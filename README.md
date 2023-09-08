# sudoku-solver

Solves a 9x9 sudoku board with constraint satisfaction

## Description

* Receives a 9x9 board with numbers from 0 to 9 and returns the number of permutations performed to solve the puzzle. During the execution, it also replaces the entries with value 0 with numbers from 1 to 9 according to the rules of the game.
* The board is represented by a 2D array
* _sudoku_backtracking_ returns an integer representing the number of recursive function calls performed to solve the board using a simple backtracking algorithm.
* _Sudoku_forwardchecking_ returns an integer representing the number of recursive function calls performed to solve the board using a forward checking algorithm.
