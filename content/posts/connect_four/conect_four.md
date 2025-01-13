---
title: "Connect 4 Game"
layout: single
draft: true
---

Enjoy a game of Connect 4 against the AI or watch two AIs play against each other!


---
title: "Connect 4 Game"
layout: single
---

<div id="game-container">
  <div id="game-board"></div>
  <div id="controls">
    <button id="new-game">New Game</button>
    <select id="player-type">
      <option value="human">Human vs AI</option>
      <option value="ai">AI vs AI</option>
    </select>
    <select id="starting-player">
      <option value="1">Yellow Starts</option>
      <option value="2">Red Starts</option>
    </select>
  </div>
  <div id="status"></div>
</div>

<script>
class Connect4 {
  constructor(rows = 6, columns = 7) {
    this.rows = rows;
    this.columns = columns;
    this.board = Array(rows).fill().map(() => Array(columns).fill(0));
    this.currentPlayer = 1;
    this.gameOver = false;
    this.winner = null;
  }

  makeMove(column) {
    if (this.gameOver || column < 0 || column >= this.columns) return false;
    
    for (let row = this.rows - 1; row >= 0; row--) {
      if (this.board[row][column] === 0) {
        this.board[row][column] = this.currentPlayer;
        this.checkWin(row, column);
        this.currentPlayer = 3 - this.currentPlayer;
        return true;
      }
    }
    
    return false;
  }

  checkWin(row, col) {
    const directions = [[0, 1], [1, 0], [1, 1], [1, -1]];
    for (let [dx, dy] of directions) {
      if (this.checkLine(row, col, dx, dy)) {
        this.gameOver = true;
        this.winner = 3 - this.currentPlayer;
        return;
      }
    }
    if (this.isFull()) {
      this.gameOver = true;
    }
  }

  checkLine(row, col, dx, dy) {
    const player = this.board[row][col];
    let count = 1;
    for (let i = 1; i <= 3; i++) {
      const r = row + i * dx;
      const c = col + i * dy;
      if (r < 0 || r >= this.rows || c < 0 || c >= this.columns || this.board[r][c] !== player) break;
      count++;
    }
    for (let i = 1; i <= 3; i++) {
      const r = row - i * dx;
      const c = col - i * dy;
      if (r < 0 || r >= this.rows || c < 0 || c >= this.columns || this.board[r][c] !== player) break;
      count++;
    }
    return count >= 4;
  }

  isFull() {
    return this.board[0].every(cell => cell !== 0);
  }

  reset() {
    this.board = Array(this.rows).fill().map(() => Array(this.columns).fill(0));
    this.currentPlayer = 1;
    this.gameOver = false;
    this.winner = null;
  }
}

class AIPlayer {
  makeMove(game) {
    const validMoves = game.board[0].map((cell, index) => cell === 0 ? index : -1).filter(index => index !== -1);
    return validMoves[Math.floor(Math.random() * validMoves.length)];
  }
}

const game = new Connect4();
const aiPlayer = new AIPlayer();
let playerTypes = { 1: 'Human', 2: 'AI' };

function createBoard() {
  const gameBoard = document.getElementById('game-board');
  gameBoard.innerHTML = '';
  for (let row = 0; row < game.rows; row++) {
    for (let col = 0; col < game.columns; col++) {
      const cell = document.createElement('div');
      cell.className = 'cell';
      cell.dataset.row = row;
      cell.dataset.col = col;
      cell.addEventListener('click', () => makeMove(col));
      gameBoard.appendChild(cell);
    }
  }
}

function updateBoard() {
  for (let row = 0; row < game.rows; row++) {
    for (let col = 0; col < game.columns; col++) {
      const cell = document.querySelector(`.cell[data-row="${row}"][data-col="${col}"]`);
      cell.className = `cell player${game.board[row][col]}`;
    }
  }
}

function updateStatus() {
  const status = document.getElementById('status');
  if (game.gameOver) {
    if (game.winner) {
      status.textContent = `Player ${game.winner === 1 ? 'Red' : 'Yellow'} wins!`;
    } else {
      status.textContent = "It's a draw!";
    }
  } else {
    status.textContent = `Current player: ${game.currentPlayer === 1 ? 'Yellow' : 'Red'}`;
  }
}

function makeMove(column) {
  if (game.makeMove(column)) {
    updateBoard();
    updateStatus();
    if (!game.gameOver && playerTypes[game.currentPlayer] === 'AI') {
      setTimeout(() => {
        const aiMove = aiPlayer.makeMove(game);
        makeMove(aiMove);
      }, 500);
    }
  }
}

function startNewGame() {
  game.reset();
  playerTypes = {
    1: document.getElementById('player-type').value === 'human' ? 'Human' : 'AI',
    2: 'AI'
  };
  game.currentPlayer = parseInt(document.getElementById('starting-player').value);
  updateBoard();
  updateStatus();
  if (playerTypes[game.currentPlayer] === 'AI') {
    makeMove(aiPlayer.makeMove(game));
  }
}

document.getElementById('new-game').addEventListener('click', startNewGame);
document.getElementById('player-type').addEventListener('change', startNewGame);
document.getElementById('starting-player').addEventListener('change', startNewGame);

createBoard();
updateBoard();
updateStatus();
</script>

<style>
#game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

#game-board {
  display: grid;
  grid-template-columns: repeat(7, 50px);
  grid-gap: 5px;
  background-color: #0066cc;
  padding: 10px;
  border-radius: 10px;
}

.cell {
  width: 50px;
  height: 50px;
  background-color: white;
  border-radius: 50%;
  cursor: pointer;
}

.player1 {
  background-color: yellow;
}

.player2 {
  background-color: red;
}

#controls {
  margin-top: 20px;
}

#status {
  margin-top: 10px;
  font-weight: bold;
}
</style>