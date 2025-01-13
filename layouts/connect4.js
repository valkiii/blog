let pyodide;
let game;

async function initializePyodide() {
  pyodide = await loadPyodide();
  await pyodide.loadPackage("numpy");
  await pyodide.runPythonAsync(await (await fetch("{{ "py/connect4.py" | relURL }}")).text());
  game = pyodide.globals.get("Connect4")();
  updateBoard();
}

function updateBoard() {
  const board = pyodide.globals.get("game").board.toJs();
  const gameBoard = document.getElementById("game-board");
  gameBoard.innerHTML = "";
  
  for (let row = 0; row < 6; row++) {
    for (let col = 0; col < 7; col++) {
      const cell = document.createElement("div");
      cell.classList.add("cell");
      if (board[row][col] !== " ") {
        const disk = document.createElement("div");
        disk.classList.add("disk", board[row][col] === "Y" ? "yellow" : "red");
        cell.appendChild(disk);
      }
      cell.addEventListener("click", () => makeMove(col));
      gameBoard.appendChild(cell);
    }
  }
  
  updateStatus();
}

function makeMove(column) {
  if (pyodide.globals.get("game").current_player === "R" && 
      document.getElementById("player-type").value === "ai") {
    return;
  }
  
  const moveResult = pyodide.globals.get("game").make_move(column);
  if (moveResult) {
    updateBoard();
    if (!pyodide.globals.get("game").game_over && 
        document.getElementById("player-type").value === "ai") {
      setTimeout(makeAIMove, 500);
    }
  }
}

function makeAIMove() {
  const aiPlayer = pyodide.globals.get("AIPlayer")();
  const move = aiPlayer.make_move(pyodide.globals.get("game"));
  pyodide.globals.get("game").make_move(move);
  updateBoard();
}

function updateStatus() {
  const statusElement = document.getElementById("status");
  if (pyodide.globals.get("game").game_over) {
    const winner = pyodide.globals.get("game").winner;
    statusElement.textContent = winner ? `Player ${winner} wins!` : "It's a draw!";
  } else {
    const currentPlayer = pyodide.globals.get("game").current_player;
    statusElement.textContent = `Current player: ${currentPlayer === "Y" ? "Yellow" : "Red"}`;
  }
}

function newGame() {
  const startingPlayer = document.getElementById("starting-player").value;
  pyodide.globals.get("game").reset();
  pyodide.globals.get("game").current_player = startingPlayer;
  updateBoard();
  
  if (startingPlayer === "R" && document.getElementById("player-type").value === "ai") {
    setTimeout(makeAIMove, 500);
  }
}

document.getElementById("new-game").addEventListener("click", newGame);
document.getElementById("player-type").addEventListener("change", newGame);
document.getElementById("starting-player").addEventListener("change", newGame);

initializePyodide();