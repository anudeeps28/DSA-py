
```
main()
├── create_board()
├── while loop:
│   ├── display_board(board)
│   ├── if current_player == 'X' (Human Turn):
│   │       ├── input()         <-- Built-in: gets user input
│   │       └── is_valid_move(board, move)
│   └── else (Computer's Turn):
│           └── get_computer_move(board)
│                   ├── find_winning_move(board, computer)
│                   │       └── check_win(board, computer)
│                   ├── find_blocking_move(board, computer, opponent)
│                   │       └── check_win(board, opponent)
│                   └── random.choice(empty_cells) <-- Built-in: selects random move
├── check_win(board, current_player)   <-- Post-move win check
└── check_draw(board)                  <-- Post-move draw check 
```
