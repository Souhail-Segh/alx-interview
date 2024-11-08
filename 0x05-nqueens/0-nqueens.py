#!/usr/bin/python3
import sys
"""N Queens Module 
"""


def calculate_N_Queens(n):
    """N Queens should be in a position
    of no attack, horizontally, vertically,
    and diagonally. It's a chess game with only
    N x N size, and exactly N Queens.
    """
    col = set()
    diagrUp = set()
    diagrDown = set()
    results = []
    chess = [[] * n]

    def backtrack_queens(row):
        """Recursion function.
        """
        if row == n:
            results.append(chess)
            

if __name__ == '__main__':
    """Check if the required arguments 
    are provided correctly and calculate.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
        
    n = sys.argv[1]
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    calculate_N_Queens(n)
