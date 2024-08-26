#!/usr/bin/python3
""" Function program that solves the N queens problem."""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    """ Print an error message, exit with a status code."""
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, a=0, i=[], b=[], c=[]):
    """ Find possible positions using backtracking"""
    if a < n:
        for j in range(n):
            if j not in i and a + j not in b and a - j not in c:
                yield from queens(n, a + 1, i + [j], b + [a + j], c + [a - j])
    else:
        yield i


def solve(n):
    """ Solve the N-Queens problem"""
    p = []
    a = 0
    for solution in queens(n, 0):
        for m in solution:
            p.append([a, m])
            a += 1
        print(p)
        p = []
        a = 0


solve(n)
