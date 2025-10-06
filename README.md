# TicTacToe

A simple, interactive command-line Tic-Tac-Toe game implemented in Python.

## Overview

This project is a classic 2-player Tic-Tac-Toe game that you play in your terminal. Players alternate turns, marking 'X' and 'O' on a 3x3 board, trying to get three of their marks in a row horizontally, vertically, or diagonally. The game automatically checks for wins and draws, and allows for restarting or exiting once a game concludes.

## Features

- **Two-player mode:** Play with a friend, taking turns on the same machine.
- **Text-based interface:** No GUI required—everything runs in your terminal.
- **Input validation:** Ensures players only make valid moves.
- **Win and draw detection:** Game announces the winner or a draw.
- **Easy restart/exit:** Continue playing or quit after each round.

## How It Works

### Game Loop

- The board is represented as a 3x3 grid.
- Players alternate entering their moves in the form `row-col` (for example, `1-3` for row 1, column 3).
- The board is printed after every valid move.
- The game checks for a win or draw after every move.
- At the end of a game, players can choose to restart or quit.

### Board Representation

The board is shown as:

```
 +---+---+---+
 | X |   | O |
 +---+---+---+
 |   | X |   |
 +---+---+---+
 | O |   | X |
 +---+---+---+
```

### Win Detection

The game considers all possible lines (rows, columns, diagonals) for a win. There are 8 possible winning combinations, such as:

- Horizontal: (0,0)-(0,1)-(0,2)
- Vertical: (0,0)-(1,0)-(2,0)
- Diagonal: (0,0)-(1,1)-(2,2), etc.

### Draw Detection

If all spaces are filled and there is no winner, the game declares a draw.

## How to Play

### Prerequisites

- Python 3 installed on your machine.

### Running the Game

1. **Clone this repository:**
   ```sh
   git clone https://github.com/jk-verse/tictactoe.git
   cd tictactoe
   ```

2. **Run the game:**
   ```sh
   python main.py
   ```

### Gameplay Instructions

- The board uses a 1-based index for both rows and columns.
- On your turn, input your move as `row-col` (e.g., `2-2` for the center square).
- If you try to move to an occupied space or outside the board, you’ll be prompted for another input.
- The game will print the board after every valid move.
- When a player wins or the board is full (draw), you’ll be prompted:
  - Enter `R` to restart the game.
  - Enter `C` to close the game.

### Example Game Session

```
 +---+---+---+
 |   |   |   |
 +---+---+---+
 |   |   |   |
 +---+---+---+
 |   |   |   |
 +---+---+---+
Row-Col: 1-1
 +---+---+---+
 | X |   |   |
 +---+---+---+
 |   |   |   |
 +---+---+---+
 |   |   |   |
 +---+---+---+
Row-Col: 2-2
...
Winner: X
Enter 'R' to restart and 'C' to close the game.
```

## Code Structure

- **main.py** - All game logic, board rendering, win/draw checks, and input handling are within this single file.

Key functions:
- `print_board()`: Renders the board.
- `is_full()`: Checks if the board is full.
- `winner()`: Checks for a winning condition.
- `game_ended()`: Determines if the game should end.

## Contributing

Pull requests and suggestions are welcome!

## License

This project is licensed under the MIT License.
