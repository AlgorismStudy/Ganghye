import sys

N = int(sys.stdin.readline())

d = dict()
for _ in range(N):
    name, type = sys.stdin.readline().split()
    if type == "enter":
        d[name] = 1
    else:
        d[name] -= 1

arr = [i for i, v in d.items() if v == 1]
arr.sort(reverse=True)

print(*arr, sep="\n")
