def new_board():
    # Create a 3x3 grid initialized with None
    return [[None for _ in range(3)] for _ in range(3)]

def render(board):
    # Print column headers
    print("  0 1 2")
    print("  ------")
    for i, row in enumerate(board):
        # Print row number
        print(f"{i}|", end="")
        # Print row content with spaces for None values
        for cell in row:
            if cell is None:
                print("  ", end="")
            else:
                print(f"{cell} ", end="")
        print("|")
    print("  ------")

def get_move():
    while True:
        try:
            # Ask the player for their move
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            
            # Validate the input
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter a row and column between 0 and 2.")
        except ValueError:
            print("Invalid format. Please enter your move as 'row,col'.")

def make_move(board, row, col, player):
    if board[row][col] is None:
        board[row][col] = player
        return True
    else:
        print("This square is already taken. Try again.")
        return False


def check_winner(board):    
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def is_draw(board):
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True 


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = None
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                board[row][col] = None
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move



def tic_tac_toe():
    board = new_board()
    current_player= "X"

    while True:
        render(board)
        if current_player == 'X':
            print("Player X's turn")
            while True:
                row, col = get_move()
                if make_move(board, row, col, current_player):
                    break
        else:
            print("AI's turn")
            input("Press Enter for the AI to make it's move.")
            move = find_best_move(board)
            if move:
                make_move(board, move[0], move[1], current_player)
        winner = check_winner(board)
        if winner:
            render(board)
            print(f"Player {winner} wins!")
            break
        # Check for draw
        if is_draw(board):
            render(board)
            print("The game is a draw!")
            break
        # Switch players
        current_player = "X" if current_player == "O" else "O"

tic_tac_toe() 
