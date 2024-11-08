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
            return

        for c in range(n):
            if c in col or (row + c) in diagrUp or \
               (row - c) in diagrDown:
                continue

            col.add(c)
            diagrUp.add(row + c)
            diagrDown.add(row - c)
            chess[row] = [row, c]

            backtrack_queens(row + 1)

            col.remove(c)
            diagrUp.remove(row + c)
            diagrDown.remove(row - c)
            chess[row] = []
            
    backtrack_queens(0)
    return (results)

if __name__ == '__main__':
    """Check if the required arguments 
    are provided correctly and calculate.
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

    print(calculate_N_Queens(n))
