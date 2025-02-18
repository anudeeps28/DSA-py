# Tic Tac Toe CLI Game

A simple command-line Tic Tac Toe game where you (the human) play against the computer. The computer uses basic strategies to win or block your moves. This project is ideal for beginners learning Python and game logic implementation.

## Features

- **Command-Line Interface (CLI):**  
  Play directly in your terminal with an easy-to-read 3x3 grid display.
  
- **Human vs. Computer Gameplay:**  
  - You play as **X** and the computer plays as **O**.
  - The computer checks for winning moves and blocks potential wins.
  
- **Game Logic:**  
  - Validates moves to ensure players can only mark empty cells.
  - Detects win conditions for rows, columns, and diagonals.
  - Detects draws when the board is full.

## How It Works

1. **Board Setup:**  
   The game board is represented as a list of 9 elements. Each element corresponds to a cell in the 3x3 grid.

2. **Game Loop:**  
   - The game alternates turns between the human player and the computer.
   - The board is displayed after each move.
   - The game checks for win conditions and a draw after every move.
   - The loop continues until there is a win or a draw.

3. **Computer AI:**  
   - The computer first checks if it can win in one move.
   - If not, it checks if it needs to block the human's winning move.
   - If neither condition is met, it selects a random empty cell.

## Function Call Diagram 
Refer --> [[Function Call Diagram]]

## Prerequisites
- **Python 3.x**
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## How to run

1. **Clone the Repository** (if using Git):
```
git clone https://github.com/yourusername/tic-tac-toe-cli.git
cd tic-tac-toe-cli
```

2. **Run the program**
Open a terminal in the project directory and execute:
```
python tic_tac_toe.py
```

1. **Play the game**
- When prompted, enter a number between 1 and 9 to place your **X**.
- The game will display the board after each move.
- Enjoy playing against the computer!