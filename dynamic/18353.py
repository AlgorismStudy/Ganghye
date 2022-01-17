n = int(input())
arr = list(map(int, input().split()))
d = [0] * (n+1)
answer = 0
arr = arr[::-1]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+1)


# 4 2 5 8 4 11 15
