const cells = document.querySelectorAll(".cell");
const statusText = document.getElementById("status");
const resultScreen = document.getElementById("resultScreen");
const resultText = document.getElementById("resultText");
const newGameBtn = document.getElementById("newGameBtn");

let board = ["", "", "", "", "", "", "", "", ""];
let gameActive = true;

const HUMAN = "X";
const AI = "O";

const winningCombinations = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

cells.forEach((cell, index) =>
  cell.addEventListener("click", () => handlePlayerMove(index))
);

function handlePlayerMove(index) {
  if (board[index] !== "" || !gameActive) return;

  makeMove(index, HUMAN);

  if (gameActive) {
    statusText.textContent = "Computer's turn 🤖";
    setTimeout(aiMove, 500);
  }
}

function makeMove(index, player) {
  board[index] = player;
  cells[index].textContent = player;

  if (checkWinner(player)) {
    endGame(player === HUMAN ? "🎉 You Win!" : "🤖 Computer Wins");
    return;
  }

  if (!board.includes("")) {
    endGame("😐 It's a Draw");
    return;
  }

  statusText.textContent = player === HUMAN ? "Computer's turn 🤖" : "Your turn";
}

function aiMove() {
  let move =
    findBestMove(AI) ??
    findBestMove(HUMAN) ??
    getRandomMove();

  makeMove(move, AI);
}

function findBestMove(player) {
  for (const combo of winningCombinations) {
    const [a, b, c] = combo;
    const values = [board[a], board[b], board[c]];

    if (values.filter(v => v === player).length === 2 && values.includes("")) {
      return combo[values.indexOf("")];
    }
  }
  return null;
}

function getRandomMove() {
  const emptyCells = board
    .map((v, i) => (v === "" ? i : null))
    .filter(v => v !== null);

  return emptyCells[Math.floor(Math.random() * emptyCells.length)];
}

function checkWinner(player) {
  return winningCombinations.some(combo =>
    combo.every(index => board[index] === player)
  );
}

function endGame(message) {
  gameActive = false;
  resultText.textContent = message;
  resultScreen.classList.remove("hidden");
}

function resetGame() {
  board = ["", "", "", "", "", "", "", "", ""];
  gameActive = true;
  statusText.textContent = "Your turn";
  cells.forEach(cell => (cell.textContent = ""));
  resultScreen.classList.add("hidden");
}

newGameBtn.addEventListener("click", resetGame);