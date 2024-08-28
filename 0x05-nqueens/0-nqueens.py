#!/usr/bin/python3
""" N queens """
import sys


def is_safe(board, row, col):
    """ function Check if there's a queen in the same column """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """ function recursively tries to place queens on the board """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1


def print_solutions(solutions):
    """ function outputs each solution in the required format """
    for solution in solutions:
        print(solution)


def main():
    """ run """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
