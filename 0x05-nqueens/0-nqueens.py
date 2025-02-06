#!/usr/bin/python3
import sys

def solve_nqueens(N):
    """Solve the N Queens problem and return all possible solutions."""
    def is_safe(board, row, col):
        """Check if a queen can be placed on board[row][col]."""
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True

    def solve(board, col, solution):
        """Backtracking function to solve N Queens."""
        # Base case: If all queens are placed, save the solution
        if col >= N:
            current_solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        current_solution.append([i, j])
            solutions.append(current_solution)
            return

        # Consider this column and try placing this queen in all rows one by one
        for i in range(N):
            if is_safe(board, i, col):
                # Place this queen in board[i][col]
                board[i][col] = 1

                # Recur to place rest of the queens
                solve(board, col + 1, solution)

                # Backtrack and remove queen from board[i][col]
                board[i][col] = 0

    # Create a board of size N x N
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    # Start from the first column
    solve(board, 0, [])
    return solutions

def main():
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print solutions
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()