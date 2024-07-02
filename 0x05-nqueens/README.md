# N Queens Solver

This project provides a solution to the N Queens problem, which involves placing N non-attacking queens on an N×N chessboard.

## Usage

To use this script, you need to have Python installed on your system. The script takes a single argument, which is the size of the chessboard (N).

### Running the script

To run the script, use the following command:

```bash
python3 0-nqueens.py N
```

### Examples
```bash
$ python3 0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ python3 0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### Requirements
> - Allowed editors: ```vi, vim, emacs```
> - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.3)
> - All your files should end with a new line
> - The first line of all your files should be exactly ```#!/usr/bin/python3```
> - A ```README.md``` file, at the root of the folder of the project, is mandatory
> - Your code should use the ```PEP 8``` style (version 1.7.*)
> - All your files must be executable

### Implementation Details
* Files<br>
**0-nqueens.py:** The main script that solves the N Queens problem.
**Script Explanation**<br>
The script performs the following tasks:

* *Argument Validation:*<br>
Checks if exactly one argument is provided.<br>
Validates whether the argument is an integer and whether it is at least 4.<br>
* *Helper Functions:*<br>
is_safe(board, row, col): Checks if a queen can be placed at the given row and<br> column without being attacked by any other queen.<br>
solve_nqueens(board, row, n, solutions): Recursively tries to place queens row by<br> row. If it reaches the end of the board (row == n), it adds the current<br> board configuration to the list of solutions.<br>
print_solutions(solutions, n): Prints each solution in the required format.<br>
* *Main Logic:*
Initializes the board with -1 (indicating no queen is placed in any column).<br>
Calls the recursive function to find all solutions.<br>
Prints the solutions.<br>
*Function Definitions*
* *is_safe(board, row, col):* Checks if placing a queen at (row, col) is safe.<br>
* *solve_nqueens(board, row, n, solutions):* Recursively solves the N Queens problem.<br>
* *print_solutions(solutions, n):* Prints the list of solutions.<br>
**Algorithm**
The algorithm uses backtracking to place queens one by one in different rows,<br> starting from the first row. It checks for clashes with already placed queens<br> and proceeds if the position is safe. If all queens are placed successfully,<br> it records the solution.<br>
**Contributing**
If you would like to contribute to this project, please fork the repository and<br> create a pull request with your changes. I welcome all improvements and <br>suggestions!

**Author**
* Ikilai Doreen - [Demidorn](https://github.com/Demidorn)