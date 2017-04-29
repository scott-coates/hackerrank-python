vals = map(int,
           "5 8 1 4 9 88 9 49 2 9 09 38 409 89 389  48 389 3908 31 1 98 3098 308 320 301 23 32 3 7 9 2".strip().split())


def build(arr):
    left = []
    eq = []
    right = []

    for i, v in enumerate(arr):
        if i == 0 or v == eq[0]:
            eq.append(v)
        else:
            if v < eq[0]: left.append(v)
            if v > eq[0]: right.append(v)

    if left:
        left = build(left)
        print(' '.join(map(str, left)))

    if right:
        right = build(right)
        print(' '.join(map(str, right)))

    all = left + eq + right

    return all


new_arr = build(vals)
print(' '.join(map(str, new_arr)))
