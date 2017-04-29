# Tower of M... something...
import requests
import sys

# input = input().split('\n')
# input = sys.stdin.read()
input = """1
4 2
7 2 8
1 2 3 4"""


def get_int_array(s):
    x = [int(n) for n in s.split(' ')]
    x = ''.join(str(y) for y in x)
    return int(x)


input_int = [get_int_array(l) for l in input.split('\n')]
# input = [1, 42, 728, 1234]

answer = 7

sum = 0
for i in range(0, len(input)):
    val = 0
    if i == 0:
        val = int(input[i])
        pivot = 0
    else:
        num_str = str(input[i])
        num_parts = [int(i) for i in num_str]
        if num_parts[pivot] <= num_parts[pivot + 1] :
            pivot = pivot
            val = int(num_parts[pivot])
        else:
            pivot = pivot + 1
            val = int(num_parts[pivot])

    sum += val

print(sum)
