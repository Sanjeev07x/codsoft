const PLAYER_X = 'X';
const PLAYER_O = 'O';
const EMPTY = ' ';
let board = [];
let currentPlayer = PLAYER_X;

// Initialize the board
function initializeBoard() {
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ];
    renderBoard();
}

// Render the board on the webpage
function renderBoard() {
    const boardDiv = document.getElementById('board');
    boardDiv.innerHTML = '';
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.innerText = board[row][col];
            cell.dataset.row = row;
            cell.dataset.col = col;
            cell.addEventListener('click', handleCellClick);
            boardDiv.appendChild(cell);
        }
    }
}

// Handle click on a cell
function handleCellClick(event) {
    const row = event.target.dataset.row;
    const col = event.target.dataset.col;

    if (board[row][col] === EMPTY && currentPlayer === PLAYER_X) {
        board[row][col] = PLAYER_X;
        currentPlayer = PLAYER_O;
        renderBoard();
        if (checkWinner(PLAYER_X)) {
            alert('Player X wins!');
            return;
        }
        if (isBoardFull()) {
            alert('It\'s a draw!');
            return;
        }
        aiMove();  // AI makes its move
    }
}

// AI Move using the Minimax algorithm
function aiMove() {
    const bestMove = minimax(board, 0, true);
    const { row, col } = bestMove;
    board[row][col] = PLAYER_O;
    currentPlayer = PLAYER_X;
    renderBoard();
    if (checkWinner(PLAYER_O)) {
        alert('AI wins!');
    } else if (isBoardFull()) {
        alert('It\'s a draw!');
    }
}

// Minimax algorithm to determine the best move for the AI
function minimax(board, depth, isMaximizing) {
    if (checkWinner(PLAYER_X)) return { score: -10 };
    if (checkWinner(PLAYER_O)) return { score: 10 };
    if (isBoardFull()) return { score: 0 };

    let bestMove = { score: isMaximizing ? -Infinity : Infinity };
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            if (board[row][col] === EMPTY) {
                board[row][col] = isMaximizing ? PLAYER_O : PLAYER_X;
                const score = minimax(board, depth + 1, !isMaximizing).score;
                board[row][col] = EMPTY;
                if (isMaximizing) {
                    if (score > bestMove.score) {
                        bestMove = { row, col, score };
                    }
                } else {
                    if (score < bestMove.score) {
                        bestMove = { row, col, score };
                    }
                }
            }
        }
    }
    return bestMove;
}

// Check if a player has won
function checkWinner(player) {
    // Check rows, columns, and diagonals
    for (let i = 0; i < 3; i++) {
        if (board[i].every(cell => cell === player)) return true;
        if (board.every(row => row[i] === player)) return true;
    }
    if (board[0][0] === player && board[1][1] === player && board[2][2] === player) return true;
    if (board[0][2] === player && board[1][1] === player && board[2][0] === player) return true;
    return false;
}

// Check if the board is full
function isBoardFull() {
    return board.every(row => row.every(cell => cell !== EMPTY));
}

// Reset the game
document.getElementById('resetButton').addEventListener('click', () => {
    initializeBoard();
    currentPlayer = PLAYER_X;
});

// Initialize the game
initializeBoard();
