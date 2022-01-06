import sys

N = int(sys.stdin.readline())
card_N = list(map(int, sys.stdin.readline().split()))
M = int(input())
card_M = list(map(int, sys.stdin.readline().split()))

d = dict()
arr = []

for i in card_N:
    if i in d:
        d[i] += 1
    if i not in d:
        d[i] = 1

for i in card_M:
    if i in d:
        arr.append(d[i])
    else:
        arr.append(0)
print(*arr, sep=" ")
