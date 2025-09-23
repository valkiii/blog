# 🚀 Hugging Face Spaces Deployment Guide

## Files Created for HF Spaces

✅ **app.py** - Main Gradio application with Flask API
✅ **requirements_hf.txt** - Python dependencies for HF Spaces  
✅ **README_HF.md** - Documentation for your HF Space
✅ **HUGGINGFACE_DEPLOYMENT.md** - This deployment guide

## 📋 Deployment Steps

### 1. Create Hugging Face Account
- Go to https://huggingface.co/join
- Create account or sign in

### 2. Create New Space
- Click "Create new" → "Space"
- **Space name:** `connect4-tournament-ai` (or your choice)
- **License:** MIT
- **SDK:** Gradio
- **Hardware:** CPU Basic (free) or upgrade for faster inference

### 3. Upload Files
Upload these files to your HF Space repository:

**Required Files:**
- `app.py` (main application)
- `requirements.txt` → rename `requirements_hf.txt` to `requirements.txt`
- `README.md` → use `README_HF.md` content
- `ensemble_agent.py`
- `game/` folder (board.py, __init__.py)
- `agents/` folder (all agent files)
- `examples/ensemble_config_v.json`
- `models_m1_cnn/` folder with your 5 tournament models:
  - `m1_cnn_dqn_ep_750000.pt`
  - `m1_cnn_dqn_ep_700000.pt` 
  - `m1_cnn_dqn_ep_650000.pt`
  - `m1_cnn_dqn_ep_600000.pt`
  - `m1_cnn_dqn_ep_550000.pt`

### 4. File Upload Methods

**Option A: Web Interface**
- Drag and drop files into the HF Space interface
- Upload folders by selecting all files

**Option B: Git (Recommended)**
```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/connect4-tournament-ai
cd connect4-tournament-ai

# Copy files from your project
cp /path/to/web_connect4_game/app.py .
cp /path/to/web_connect4_game/requirements_hf.txt requirements.txt
cp /path/to/web_connect4_game/README_HF.md README.md
cp /path/to/web_connect4_game/ensemble_agent.py .
cp -r /path/to/web_connect4_game/game .
cp -r /path/to/web_connect4_game/agents .
cp -r /path/to/web_connect4_game/examples .
cp -r /path/to/web_connect4_game/models_m1_cnn .

# Commit and push
git add .
git commit -m "Deploy Connect 4 Tournament AI ensemble"
git push
```

### 5. Space Configuration
Your Space will automatically:
- ✅ Install dependencies from requirements.txt
- ✅ Run app.py 
- ✅ Provide Gradio web interface
- ✅ Expose API endpoints at `/api/move` and `/health`

### 6. Get Your API URL
After deployment, your Space URL will be:
`https://huggingface.co/spaces/YOUR_USERNAME/connect4-tournament-ai`

API endpoint:
`https://YOUR_USERNAME-connect4-tournament-ai.hf.space/api/move`

## 🔧 Testing Your Deployment

### Test Web Interface
Visit your Space URL and try playing the game

### Test API Endpoint
```bash
curl -X POST https://YOUR_USERNAME-connect4-tournament-ai.hf.space/api/move \
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

## 📦 Model Size Considerations

Your models total ~500MB. HF Spaces free tier supports this, but consider:
- **Free tier:** Works but may be slower
- **Upgrade to GPU:** Faster inference for better user experience
- **Model optimization:** Consider model quantization if needed

## 🌐 Next Steps

Once deployed:
1. ✅ Test the HF Space works
2. ✅ Get your API endpoint URL  
3. ✅ Update your blog's frontend to use the HF API
4. ✅ Deploy updated blog

Your tournament AI will then be live and accessible to all blog visitors!

## 🎯 Expected Result

Your HF Space will provide:
- **Web interface** for direct play
- **REST API** for your blog integration
- **Public access** for anyone to play against your tournament AI
- **24/7 availability** with automatic scaling