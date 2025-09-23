# 🔴 Connect 4 Tournament AI 🟡

This is the tournament-winning Connect 4 AI ensemble that achieved #1 ranking with a 63.4% win rate against 35+ AI opponents.

## 🏆 AI Architecture

**Custom-Ensemble-Top5Models-q** combines 5 CNN-based Deep Q-Networks:
- **M1-CNN-750k** (weight: 30%) - 750,000 training episodes
- **M1-CNN-700k** (weight: 20%) - 700,000 training episodes  
- **M1-CNN-650k** (weight: 20%) - 650,000 training episodes
- **M1-CNN-600k** (weight: 15%) - 600,000 training episodes
- **M1-CNN-550k** (weight: 15%) - 550,000 training episodes

**Decision Method:** Q-value averaging with weighted ensemble voting

## 🎮 How to Use

### Web Interface
Play directly in the Gradio interface above! Enter a column number (1-7) to make your move.

### API Usage
You can integrate this AI into your own applications:

```bash
curl -X POST https://yourspace.hf.space/api/move \
  -H "Content-Type: application/json" \
  -d '{
    "board": [
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,1,0,0,0]
    ]
  }'
```

**Response:**
```json
{
  "move": 3,
  "legal_moves": [0,1,2,3,4,5,6],
  "ensemble_method": "q_value_averaging",
  "model_count": 5
}
```

### Board Format
- `0` = Empty cell
- `1` = Human player (red)
- `2` = AI player (yellow)
- Board is 6 rows × 7 columns (top to bottom, left to right)

## 🧠 Technical Details

- **Framework:** PyTorch Deep Q-Networks
- **Architecture:** Convolutional Neural Networks optimized for Connect 4
- **Training:** Multi-stage training with experience replay and target networks
- **Ensemble Method:** Weighted Q-value averaging for robust decision making
- **Performance:** Tournament winner with 63.4% win rate

## 🔧 Integration

This Space provides both a web interface and REST API endpoints for easy integration into websites, games, and applications.

**Health Check:** `GET /health`
**AI Move:** `POST /api/move`

Perfect for embedding in blogs, educational platforms, or game development!