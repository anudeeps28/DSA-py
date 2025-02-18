# board representation
def create_board():
    """Create an empty board represented as a list of 9 spaces."""
    return [' ' for _ in range(9)]

def display_board(board):
    """Display the current state of the board in a 3x3 grid."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# move validation
def is_valid_move(board, move):
    """
    Check if the move is valid.
    move: an integer (1-9) corresponding to the board cell.
    Returns True if valid (cell is empty), else False.
    """
    index = move - 1  # Convert user input (1-indexed) to 0-indexed list
    return 0 <= index < 9 and board[index] == ' '

# win and draw detection
# Define winning combinations as tuples of indices.
winning_combinations = [
    (0, 1, 2),  # Top row
    (3, 4, 5),  # Middle row
    (6, 7, 8),  # Bottom row
    (0, 3, 6),  # Left column
    (1, 4, 7),  # Middle column
    (2, 5, 8),  # Right column
    (0, 4, 8),  # Diagonal from top-left to bottom-right
    (2, 4, 6)   # Diagonal from top-right to bottom-left
]

def check_win(board, player):
    """Return True if the player has a winning combination on the board."""
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_draw(board):
    """Return True if the board is full and no win has been detected."""
    return all(cell != ' ' for cell in board)

# computer AI
def find_winning_move(board, player):
    """
    Check if 'player' (computer) can win in one move.
    Returns the index (0-8) of the winning move if found, otherwise None.
    """
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = player
            if check_win(board, player):
                board[i] = ' '  # Revert the move
                return i
            board[i] = ' '  # Revert the move
    return None

def find_blocking_move(board, computer, opponent):
    """
    Check if the opponent is about to win.
    Returns the index (0-8) where the computer can block the opponent.
    """
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = opponent
            if check_win(board, opponent):
                board[i] = ' '  # Revert the move
                return i
            board[i] = ' '  # Revert the move
    return None

import random
def get_computer_move(board, computer='O', opponent='X'):
    # 1. Check for a winning move
    move = find_winning_move(board, computer)
    if move is not None:
        return move

    # 2. Check for a blocking move
    move = find_blocking_move(board, computer, opponent)
    if move is not None:
        return move

    # 3. Otherwise, choose a random empty cell
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    return random.choice(empty_cells) if empty_cells else None

# main game loop
def main():
    board = create_board()
    current_player = 'X'  # Human starts first
    
    while True:
        display_board(board)
        
        # Human turn
        if current_player == 'X':
            try:
                move = int(input("Enter your move (1-9): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            
            if not is_valid_move(board, move):
                print("That move is not valid. Try again.")
                continue
            
            board[move - 1] = 'X'
        else:
            # Computer turn
            print("Computer's turn:")
            move = get_computer_move(board)
            board[move] = 'O'
        
        # Check for a win
        if check_win(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        # Switch turns
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()

