from re import L


n = int(input())
arr = []

for _ in range(n):
    x, y, z = map(int, input().split())
    arr.append((x, y, z))

for i in range(3):
    arr.sort(key=lambda x: x[i])
    for j in range(n):
        if j == n-1:
            dist = arr[j][i] - arr[0][i]

        else:
            dist = arr[j][i] - arr[j+1][i]
