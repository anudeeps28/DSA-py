```
main()
├── parse_command_line_args()
├── initialize_board(rows, cols, mines)
│       ├── place_mines(board, mines)
│       └── calculate_adjacent_mines(board)
├── game_loop()
│       ├── print_board(board)
│       ├── get_user_input()
│       ├── process_input(input_str)
│       └── process_command(board, command)
│               ├── reveal_cell(board, row, col)
│               │       └── flood_fill(board, row, col)
│               └── toggle_flag(board, row, col)
├── check_win_condition(board)
└── end_game(win)
```
