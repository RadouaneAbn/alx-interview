#!/usr/bin/python3

import sys


def is_safe(x, y, n, all_pos):
    """ This function checked if the position of the queen is safe """
    for pos in all_pos:
        if pos is None:
            continue
        if y == pos[0] or x == pos[1] or abs(y - pos[0]) == abs(x - pos[1]):
            return False
    all_pos[y] = [y, x]
    return True


def start_rec(all_pos, y, n):
    """ This function start the recursion preccess to find all possible
        safe positions of the queens """
    if y == n:
        print(all_pos)
        return

    for x in range(n):
        if is_safe(x, y, n, all_pos):
            start_rec(all_pos, y + 1, n)
            all_pos[y] = None


def nqueens(n):
    """ This function starts the nqueen recursion """
    for i in range(n):
        all_pos = [None for _ in range(n)]
        all_pos[0] = [0, i]
        start_rec(all_pos, 1, n)


if __name__ == "__main__":
    """ Entry point """
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
    nqueens(n)
