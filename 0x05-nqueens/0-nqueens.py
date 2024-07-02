import sys

def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False
        # Check the diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1

def print_solutions(solutions, n):
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])

def main():
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
