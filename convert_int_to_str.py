# convert 123 to "123"
# mod 3
# integer division


def num(n):
    str = ""
    while n > 0:
        new_num = n % 10
        str = chr(48 + new_num) + str
        n = n // 10
    return str


s = num(123)
print(s)
