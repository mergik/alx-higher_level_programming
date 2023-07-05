#!/usr/bin/python3
"""
N Queens Puzzle Solver

The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard.

Usage: nqueens N
    If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line,
    and exit with the status 1
where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line,
    and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a new line,
    and exit with the status 1
The program should print every possible solution to the problem
    One solution per line
    Format: see example
You are only allowed to import the sys module
"""

import sys


class NQueensSolver:
    def is_safe(self, board, row, col):
        """
        Check if it's safe to place a queen at the given position.

        Args:
            board (list): The chessboard configuration.
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check if there is a queen in the upper-left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check if there is a queen in the upper-right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def solve_nqueens(self, n):
        """
        Solve the N queens problem.

        Args:
            n (int): The size of the chessboard and the number of queens.

        Returns:
            list: A list of all possible solutions to the problem.
        """

        def backtrack(board, row, solutions):
            if row == n:
                solutions.append([[i, board[i].index('Q')] for i in range(n)])
                return

            for col in range(n):
                if self.is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1, solutions)
                    board[row][col] = '.'

        solutions = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0, solutions)
        return solutions


if __name__ == '__main__':
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse and validate the value of N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem and print the solutions
    solver = NQueensSolver()
    solutions = solver.solve_nqueens(N)
    for solution in solutions:
        print(solution)
