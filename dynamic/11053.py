n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0] = 1
for i in range(1, n):
    for j in arr:
        if j

print(d)
