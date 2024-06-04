# Tic Tac Toe AI

This is a command-line implementation of the classic Tic Tac Toe game with an AI opponent. The AI uses the Minimax algorithm with alpha-beta pruning to make its moves.

## How to Run

1. Make sure you have Python 3 installed on your system.
2. Download or clone the repository to your local machine.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the following command to start the game: `python main.py`

## How to Play

1. The game will display the initial empty 3x3 board.
2. When it's your turn (Player X), enter the row and column numbers (0, 1, or 2) to make your move.
3. After you make your move, press Enter, and the AI (Player O) will make its move.
4. The game will continue until there is a winner or it ends in a draw.
5. If you want to play again, simply run the `main.py` file again.

## Code Overview

The main functionality of the game is contained in the `main.py` file. Here's a brief overview of the functions:

- `new_board()`: Creates a new 3x3 board represented as a list of lists.
- `render(board)`: Prints the current state of the board to the console.
- `get_move()`: Prompts the user to enter a valid row and column for their move.
- `make_move(board, row, col, player)`: Places the player's mark on the board at the specified row and column if the square is empty.
- `check_winner(board)`: Checks if there is a winner on the board and returns the winner's mark ('X' or 'O') or None if there is no winner.
- `is_draw(board)`: Checks if the game has ended in a draw (i.e., no more empty squares and no winner).
- `minimax(board, depth, is_maximizing)`: Implements the Minimax algorithm with alpha-beta pruning to evaluate the best move for the AI player.
- `find_best_move(board)`: Finds the best move for the AI player by calling the `minimax` function.
- `tic_tac_toe()`: The main game loop that alternates between the player's and AI's moves, checks for a winner or draw, and renders the board.

Feel free to explore the code and modify it as needed.
