import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
d = [0] * n
d[0] = arr[0]

for i in range(1, n):
    if i == 1:
        d[i] = max(arr[i-1]+arr[i], arr[i])
    elif i == 2:
        d[i] = max(arr[i-2]+arr[i], arr[i-1]+arr[i])
    else:
        d[i] = max(d[i-3]+arr[i-1]+arr[i], d[i-2]+arr[i])

print(d[-1])
# 92%에서 런타임에러(배열인덱스 오류났던 이유: for문을 3부터 돌렸을때, n이 1or2이면 오류가 난다)
# https://sungmin-joo.tistory.com/18
