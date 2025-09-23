#!/usr/bin/env python3
"""
Hugging Face Spaces app for Connect 4 Ensemble AI
Serves the tournament-winning ensemble via Gradio interface and API endpoints
"""

import os
import sys
import json
import logging
import traceback
from typing import Dict, List, Optional
import numpy as np
import gradio as gr
from flask import Flask, request, jsonify
import threading

# Add current directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

try:
    from ensemble_agent import EnsembleAgent
    from game.board import Connect4Board
except ImportError as e:
    print(f"❌ Failed to import required modules: {e}")
    print("Current directory:", current_dir)
    print("Python path:", sys.path)
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables
ensemble_agent = None
game_board = None
model_info = None


def load_ensemble_from_config(config_path: str = None) -> EnsembleAgent:
    """Load ensemble from JSON configuration or use default Top5Models-q."""
    
    # Default configuration matching examples/ensemble_config_v.json
    default_config = {
        "name": "Custom-Ensemble-Top5Models-q",
        "method": "q_value_averaging",
        "models": [
            {
                "path": "models_m1_cnn/m1_cnn_dqn_ep_750000.pt",
                "weight": 0.3,
                "name": "M1-CNN-750k"
            },
            {
                "path": "models_m1_cnn/m1_cnn_dqn_ep_700000.pt",
                "weight": 0.2,
                "name": "M1-CNN-700k"
            },
            {
                "path": "models_m1_cnn/m1_cnn_dqn_ep_650000.pt",
                "weight": 0.2,
                "name": "M1-CNN-650k"
            },
            {
                "path": "models_m1_cnn/m1_cnn_dqn_ep_600000.pt",
                "weight": 0.15,
                "name": "M1-CNN-600k"
            },
            {
                "path": "models_m1_cnn/m1_cnn_dqn_ep_550000.pt",
                "weight": 0.15,
                "name": "M1-CNN-550k"
            }
        ]
    }
    
    if config_path and os.path.exists(config_path):
        logger.info(f"Loading ensemble config from {config_path}")
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        logger.info("Using default Top5Models-q configuration")
        config = default_config
    
    # Convert to full paths
    base_dir = current_dir
    for model_config in config["models"]:
        if not model_config["path"].startswith("/") and model_config["path"] not in ["heuristic", "random"]:
            model_config["path"] = os.path.join(base_dir, model_config["path"])
    
    # Create ensemble agent
    return EnsembleAgent(
        model_configs=config["models"],
        ensemble_method=config["method"],
        player_id=2,  # AI is player 2
        name=config["name"],
        show_contributions=True
    )


def initialize_ensemble():
    """Initialize the ensemble agent."""
    global ensemble_agent, game_board, model_info
    
    try:
        logger.info("🚀 Initializing Connect 4 Ensemble AI...")
        
        # Try to load from examples/ensemble_config_v.json first
        config_path = os.path.join(current_dir, "examples", "ensemble_config_v.json")
        ensemble_agent = load_ensemble_from_config(config_path)
        
        # Initialize game board
        game_board = Connect4Board()
        
        # Store model information
        model_info = ensemble_agent.get_model_info()
        
        logger.info("✅ Ensemble initialized successfully!")
        logger.info(f"   Ensemble: {ensemble_agent.name}")
        logger.info(f"   Method: {ensemble_agent.ensemble_method}")
        logger.info(f"   Models: {len(ensemble_agent.models)}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize ensemble: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False


def get_ai_move_api(board_state: List[List[int]]) -> Dict:
    """Get AI move for current board state (API format)."""
    if not ensemble_agent:
        return {"error": "Ensemble not loaded"}
    
    try:
        # Validate board format (6x7 array)
        if not isinstance(board_state, list) or len(board_state) != 6:
            return {"error": "Board must be a 6x7 array"}
        
        for row in board_state:
            if not isinstance(row, list) or len(row) != 7:
                return {"error": "Each row must have 7 columns"}
            for cell in row:
                if cell not in [0, 1, 2]:
                    return {"error": "Board cells must be 0, 1, or 2"}
        
        # Convert to numpy array for the AI
        board_array = np.array(board_state, dtype=int)
        
        # Get legal moves
        legal_moves = []
        for col in range(7):
            if board_array[0][col] == 0:  # Top row is empty
                legal_moves.append(int(col))
        
        if not legal_moves:
            return {"error": "No legal moves available"}
        
        # Get AI move
        ai_move_raw = ensemble_agent.choose_action(board_array, legal_moves)
        
        # Convert to Python int safely
        if hasattr(ai_move_raw, 'item'):
            ai_move = int(ai_move_raw.item())
        else:
            ai_move = int(ai_move_raw)
        
        logger.info(f"AI chose move: {ai_move}")
        
        # Response with basic data
        response_data = {
            "move": int(ai_move),
            "legal_moves": legal_moves,
            "ensemble_method": ensemble_agent.ensemble_method,
            "model_count": len(ensemble_agent.models)
        }
        
        return response_data
        
    except Exception as e:
        logger.error(f"Error in get_ai_move_api: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return {"error": f"Internal server error: {str(e)}"}


def play_move_gradio(board_state, column):
    """Play a move in the Gradio interface."""
    if not ensemble_agent:
        return board_state, "❌ AI not loaded"
    
    try:
        # Convert board state to numpy array
        if isinstance(board_state, str):
            # Parse JSON string if needed
            board_state = json.loads(board_state)
        
        board = np.array(board_state)
        col = int(column) - 1  # Convert to 0-indexed
        
        # Validate move
        if col < 0 or col >= 7 or board[0][col] != 0:
            return board_state, "❌ Invalid move"
        
        # Make human move
        for row in range(5, -1, -1):
            if board[row][col] == 0:
                board[row][col] = 1
                break
        
        # Check if human won
        # (Simple win check - you can implement full logic)
        
        # Get AI move
        result = get_ai_move_api(board.tolist())
        if "error" in result:
            return board.tolist(), f"❌ AI Error: {result['error']}"
        
        ai_col = result["move"]
        
        # Make AI move
        for row in range(5, -1, -1):
            if board[row][ai_col] == 0:
                board[row][ai_col] = 2
                break
        
        return board.tolist(), f"✅ You played column {column}, AI played column {ai_col + 1}"
        
    except Exception as e:
        return board_state, f"❌ Error: {str(e)}"


def create_gradio_interface():
    """Create the Gradio interface."""
    
    # Initialize empty board
    empty_board = [[0 for _ in range(7)] for _ in range(6)]
    
    with gr.Blocks(title="🔴 Connect 4 vs Tournament AI 🟡") as iface:
        gr.Markdown("# 🔴 Connect 4 vs Tournament AI 🟡")
        gr.Markdown("**Play against the tournament-winning AI ensemble!**")
        gr.Markdown("This AI combines 5 CNN models trained on 150k-750k games each.")
        
        with gr.Row():
            with gr.Column():
                board_display = gr.JSON(value=empty_board, label="Game Board (0=empty, 1=you, 2=AI)")
                column_input = gr.Number(value=1, minimum=1, maximum=7, step=1, label="Your move (column 1-7)")
                play_button = gr.Button("Play Move", variant="primary")
                status_output = gr.Textbox(label="Game Status", interactive=False)
                
            with gr.Column():
                gr.Markdown("### 🤖 AI Information")
                if model_info:
                    gr.Markdown(f"**Ensemble:** {model_info.get('name', 'N/A')}")
                    gr.Markdown(f"**Method:** {model_info.get('method', 'N/A')}")
                    gr.Markdown(f"**Models:** {len(model_info.get('models', []))}")
                
                reset_button = gr.Button("New Game", variant="secondary")
        
        # Event handlers
        play_button.click(
            fn=play_move_gradio,
            inputs=[board_display, column_input],
            outputs=[board_display, status_output]
        )
        
        reset_button.click(
            fn=lambda: (empty_board, "New game started!"),
            outputs=[board_display, status_output]
        )
        
        gr.Markdown("### 🌐 API Endpoint")
        gr.Markdown("You can also use this Space as an API:")
        gr.Markdown("**POST** `/api/move` with JSON: `{\"board\": [[0,0,0,0,0,0,0], ...]}`")
    
    return iface


def create_flask_api():
    """Create Flask API for external calls."""
    app = Flask(__name__)
    
    @app.route('/api/move', methods=['POST'])
    def api_move():
        """API endpoint for getting AI moves."""
        try:
            data = request.get_json()
            if not data or 'board' not in data:
                return jsonify({"error": "Missing 'board' in request"}), 400
            
            result = get_ai_move_api(data['board'])
            return jsonify(result)
            
        except Exception as e:
            logger.error(f"API error: {e}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/health', methods=['GET'])
    def health():
        """Health check endpoint."""
        return jsonify({
            "status": "healthy",
            "ensemble_loaded": ensemble_agent is not None,
            "model_info": model_info
        })
    
    return app


def run_flask_api():
    """Run Flask API in a separate thread."""
    app = create_flask_api()
    app.run(host='0.0.0.0', port=7860, debug=False)


if __name__ == "__main__":
    # Initialize the ensemble
    if not initialize_ensemble():
        logger.error("Failed to initialize ensemble. Exiting.")
        sys.exit(1)
    
    # Start Flask API in background thread
    flask_thread = threading.Thread(target=run_flask_api, daemon=True)
    flask_thread.start()
    
    # Create and launch Gradio interface
    iface = create_gradio_interface()
    iface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    )