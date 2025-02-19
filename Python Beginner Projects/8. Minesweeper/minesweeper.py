# allow users to optionally specify board dimensions and the number of mines.
import argparse
def parse_command_line_args():
    """
    Parse command-line arguments for board configuration.
    Returns:
        rows (int): Number of rows in the board.
        cols (int): Number of columns in the board.
        mines (int): Number of mines to place on the board.
    """
    parser = argparse.ArgumentParser(description="CLI Minesweeper")
    parser.add_argument("--rows", type=int, default=9, help="Number of rows in the board")
    parser.add_argument("--cols", type=int, default=9, help="Number of columns in the board")
    parser.add_argument("--mines", type=int, default=10, help="Number of mines on the board")
    
    args = parser.parse_args()
    return args.rows, args.cols, args.mines

# create the 2D grid (board) and set up each cell as a dictionary. 
import random
def initialize_board(rows, cols, mines):
    """
    Initialize the game board.
    
    Args:
        rows (int): Number of rows.
        cols (int): Number of columns.
        mines (int): Number of mines to place.
        
    Returns:
        board (list of list): 2D board representation.
    """
    # Create board: a 2D list of dictionaries for each cell
    board = [
        [{"is_mine": False, "adjacent_mines": 0, "is_revealed": False, "is_flagged": False} for _ in range(cols)]
        for _ in range(rows)
    ]
    
    place_mines(board, mines)
    calculate_adjacent_mines(board)
    
    return board

# randomly place the specified number of mines on the board
def place_mines(board, mines):
    """
    Randomly place mines on the board.
    
    Args:
        board (list of list): The game board.
        mines (int): Number of mines to place.
    """
    rows = len(board)
    cols = len(board[0])
    total_cells = rows * cols
    
    # Get unique positions for mines using random.sample
    mine_positions = random.sample(range(total_cells), mines)
    
    for pos in mine_positions:
        row = pos // cols
        col = pos % cols
        board[row][col]["is_mine"] = True

# calculate adjcent mines
def calculate_adjacent_mines(board):
    """
    Calculate the number of adjacent mines for each cell.
    
    Args:
        board (list of list): The game board.
    """
    rows = len(board)
    cols = len(board[0])
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col]["is_mine"]:
                continue
            # Check all adjacent cells (8 neighbors)
            count = 0
            for r in range(max(0, row-1), min(rows, row+2)):
                for c in range(max(0, col-1), min(cols, col+2)):
                    if board[r][c]["is_mine"]:
                        count += 1
            board[row][col]["adjacent_mines"] = count

# print the current state of the board
def print_board(board, reveal_all=False):
    """
    Print the board to the CLI.
    
    Args:
        board (list of list): The game board.
        reveal_all (bool): If True, reveal all cells (used at game end).
    """
    rows = len(board)
    cols = len(board[0])
    
    # Print column numbers for clarity
    header = "   " + " ".join([str(c).rjust(2) for c in range(cols)])
    print(header)
    print("   " + "-" * (cols * 3))
    
    for i in range(rows):
        row_display = f"{i:2}|"
        for j in range(cols):
            cell = board[i][j]
            char = " "
            if reveal_all or cell["is_revealed"]:
                if cell["is_mine"]:
                    char = "*"
                elif cell["adjacent_mines"] > 0:
                    char = str(cell["adjacent_mines"])
                else:
                    char = " "
            elif cell["is_flagged"]:
                char = "F"
            else:
                char = "#"
            row_display += f" {char}"
        print(row_display)
    print()

# get user input
def get_user_input():
    """
    Get input from the user.
    
    Returns:
        str: The raw input string.
    """
    return input("Enter command (e.g., r 3 4 to reveal or f 3 4 to flag): ")

def process_input(input_str):
    """
    Parse the raw input string into a command.
    
    Args:
        input_str (str): The raw input string.
    
    Returns:
        tuple: (action, row, col) if valid, else None.
               action: 'r' for reveal, 'f' for flag.
    """
    parts = input_str.strip().split()
    if len(parts) != 3:
        print("Invalid command format. Please use: [r|f] row col")
        return None
    
    action, row_str, col_str = parts
    if action not in ("r", "f"):
        print("Invalid action. Use 'r' to reveal or 'f' to flag.")
        return None
    
    try:
        row = int(row_str)
        col = int(col_str)
    except ValueError:
        print("Row and column must be integers.")
        return None
    
    return action, row, col

def process_command(board, command):
    """
    Process the user command.
    
    Args:
        board (list of list): The game board.
        command (tuple): Parsed command (action, row, col).
        
    Returns:
        bool: True if a mine was revealed (game over), False otherwise.
    """
    action, row, col = command
    rows = len(board)
    cols = len(board[0])
    
    # Check bounds
    if row < 0 or row >= rows or col < 0 or col >= cols:
        print("Coordinates out of bounds.")
        return False
    
    if action == "r":
        return reveal_cell(board, row, col)
    elif action == "f":
        toggle_flag(board, row, col)
        return False
    

def reveal_cell(board, row, col):
    """
    Reveal a cell. If the cell has zero adjacent mines, use flood fill.
    
    Args:
        board (list of list): The game board.
        row (int): Row index.
        col (int): Column index.
    
    Returns:
        bool: True if a mine was revealed (loss), False otherwise.
    """
    cell = board[row][col]
    
    if cell["is_revealed"]:
        return False  # already revealed, do nothing
    if cell["is_flagged"]:
        print("Cell is flagged. Unflag it before revealing.")
        return False
    
    cell["is_revealed"] = True
    
    if cell["is_mine"]:
        return True  # mine revealed, game over
    
    if cell["adjacent_mines"] == 0:
        flood_fill(board, row, col)
    
    return False

from collections import deque

def flood_fill(board, start_row, start_col):
    """
    Reveal all contiguous cells with zero adjacent mines using BFS.

    Args:
        board (list of list): The game board.
        start_row (int): Starting row index.
        start_col (int): Starting column index.
    """
    rows, cols = len(board), len(board[0])
    queue = deque([(start_row, start_col)])
    visited = set()  # To prevent revisiting cells

    # Directions for the 8 neighboring cells
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    while queue:
        row, col = queue.popleft()

        # Skip if out of bounds or already visited
        if (row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited):
            continue

        cell = board[row][col]

        # Skip flagged or already revealed cells
        if cell["is_flagged"] or cell["is_revealed"]:
            continue

        # Reveal the cell and mark as visited
        cell["is_revealed"] = True
        visited.add((row, col))

        # If the cell has zero adjacent mines, enqueue its neighbors
        if cell["adjacent_mines"] == 0 and not cell["is_mine"]:
            for dr, dc in directions:
                queue.append((row + dr, col + dc))

def toggle_flag(board, row, col):
    """
    Toggle the flagged state of a cell.
    
    Args:
        board (list of list): The game board.
        row (int): Row index.
        col (int): Column index.
    """
    cell = board[row][col]
    if cell["is_revealed"]:
        print("Cannot flag a revealed cell.")
    else:
        cell["is_flagged"] = not cell["is_flagged"]

def check_win_condition(board):
    """
    Check if the game has been won (all non-mine cells are revealed).
    
    Args:
        board (list of list): The game board.
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    for row in board:
        for cell in row:
            if not cell["is_mine"] and not cell["is_revealed"]:
                return False
    return True

def end_game(win, board):
    """
    End the game by revealing the entire board and printing a final message.
    
    Args:
        win (bool): True if the player has won, False if lost.
        board (list of list): The game board.
    """
    print_board(board, reveal_all=True)
    if win:
        print("Congratulations! You've won!")
    else:
        print("Game Over! You hit a mine.")


def main():
    # Parse command-line arguments
    rows, cols, mines = parse_command_line_args()
    
    # Initialize the board
    board = initialize_board(rows, cols, mines)
    
    game_over = False
    while not game_over:
        print_board(board)
        user_input = get_user_input()
        command = process_input(user_input)
        if command is None:
            continue  # invalid input, ask again
        
        # Process the command. If reveal_cell returns True, a mine was hit.
        if process_command(board, command):
            game_over = True
            end_game(False, board)
            break
        
        # Check win condition after each valid command
        if check_win_condition(board):
            game_over = True
            end_game(True, board)
            break

if __name__ == "__main__":
    main()