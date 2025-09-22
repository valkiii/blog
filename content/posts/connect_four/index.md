---
title: "🔴 Connect 4 vs AI Ensemble 🟡"
date: 2025-01-01T01:01:01Z
draft: false
categories: ["coding", "free-time"]
tags: ["competition", "coding"]
featured_image: ""
description: "Challenge a tournament-winning AI ensemble in Connect 4! This AI combines 5 neural networks trained on 750k games and won first place against 35+ AI opponents."
---

Challenge our tournament-winning AI system in Connect 4! This isn't just any AI - it's an ensemble of 5 neural networks that dominated a comprehensive tournament against 35+ other AI opponents.

## The AI Opponent

You're playing against **"Custom-Ensemble-Top5Models-q"** - a sophisticated AI system that:

- **Combines 5 CNN-based Deep Q-Networks** trained on 150k-750k games each
- **Uses Q-value averaging** for strategic decision making  
- **Achieved #1 ranking** with 63.4% win rate in tournament play
- **Applies weighted strategy** (30%, 20%, 20%, 15%, 15%) based on model performance

---

{{< connect4 >}}

## How the AI Works

### 🔗 Ensemble Architecture
Combines 5 CNN-based Deep Q-Networks trained on different amounts of gameplay experience (150k-750k episodes each)

### 🎯 Q-Value Averaging  
Each model predicts Q-values for all moves, then weights are applied and averaged for final decision

### ⚖️ Weighted Strategy
Model weights: 30%, 20%, 20%, 15%, 15% based on training progression and performance

### 🏆 Tournament Proven
Winner of comprehensive tournament against 35+ AI opponents including other ensembles and individual models

---

**Controls:** Click columns to drop pieces, or use keyboard shortcuts 1-7. Press 'H' for hints, 'N' for new game.