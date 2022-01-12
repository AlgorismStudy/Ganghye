# 메모리 초과
from itertools import combinations
import sys

n, c = map(int, sys.stdin.readline().split())
home = []
distances = []

for i in range(n):
    home.append(int(sys.stdin.readline()))
home.sort()
print("h:", home)

for i in range(1, n):
    distances.append(home[i] - home[i - 1])
print("D:", distances)

lines = list(combinations(home, c))
print(lines)
arr = []
points = []
for i in lines:
    temp = []
    for j in range(1, len(i)):
        temp.append(i[j] - i[j - 1])

    if arr:
        if min(temp) > min(arr):
            arr = temp
            points = i
    else:
        arr = temp
        points = i

print(min(arr))
