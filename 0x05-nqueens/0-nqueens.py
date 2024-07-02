#!/usr/bin/python3


"""
N Queens Solver

This script solves the N Queens problem, which involves placing
N non-attacking queens on an N×N chessboard.
It takes a single argument, N, which must be an integer greater
than or equal to 4.
The script prints all possible solutions where each solution is
a list of positions of the queens.

Usage:
    python3 0-nqueens.py N

Arguments:
    N (int): The size of the chessboard and the number of queens.

Example:
    python3 0-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""


import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.

    Args:
    board (list): The current state of the chessboard.
    row (int): The row index where the queen is to be placed.
    col (int): The column index where the queen is to be placed.

    Returns:
    bool: True if the position is safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col:
            return False
        # Check the diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Solve the N Queens problem using backtracking.

    Args:
    board (list): The current state of the chessboard.
    row (int): The current row index being processed.
    n (int): The size of the chessboard.
    solutions (list): The list to store all the valid solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1


def print_solutions(solutions, n):
    """
    Print all the solutions to the N Queens problem.

    Args:
    solutions (list): The list of all valid solutions.
    n (int): The size of the chessboard.
    """
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


def main():
    """
    Main function to handle input and trigger the N Queens solution process.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions, n)


if __name__ == "__main__":
    main()
