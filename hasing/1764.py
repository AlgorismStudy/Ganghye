import sys

N, M = map(int, sys.stdin.readline().split())
d = dict()
arr = []

for i in range(N + M):
    name = input()
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1
    if d[name] >= 2:
        arr.append(name)

arr = sorted(arr)

print(len(arr), *arr, sep="\n")
