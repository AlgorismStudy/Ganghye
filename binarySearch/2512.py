# 떡자르기같은문제
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

arr.sort()

left = 0
right = max(arr)

while left <= right:
    total = 0
    mid = (left + right) // 2
    for i in arr:
        if i >= mid:
            total += mid
        else:
            total += i
    if total <= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
