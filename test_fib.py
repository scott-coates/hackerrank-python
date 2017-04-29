def fib1(n):
    def n1():
        print('starting n-1', n)
        return fib1(n - 1)

    def n2():
        print('starting n-2', n)
        return fib1(n - 2)

    if n == 0:
        return 0
    if n == 1:
        return 1
    return n1() + n2()


# x = fib1(6000)
# print(x)

def fib2(n):
    a, b = 1, 1,
    for i in range(n-1):
        a, b = b, a + b
    return a


x = fib2(44)
print(x)
