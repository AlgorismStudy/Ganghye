from itertools import combinations

cases = int(input())
d = dict()
arr = []
for _ in range(cases):
    case = int(input())

    for _ in range(case):
        _, type = input().split()
        if type in d:
            d[type] += 1
        else:
            d[type] = 1

    l = list(d.values())
    res = 1

    for i in l:
        res *= i + 1
    arr.append(res - 1)
    d = dict()
print(*arr, sep="\n")
