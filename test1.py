# n = int(input())
# for i in range(n):
#     a, b = input().strip().split(' ')
#     print(int(a) + int(b))
# !/bin/python3

import sys

# _n = int(input());
_n = 6


def StairCase(n):
    str = ''
    for i in range(1, n + 1):
        s = ''.join(('#' for a in range(1, i + 1)))
        s = s.rjust(n, ' ')
        print(s)


StairCase(_n)
