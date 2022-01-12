n = int(input())
k = int(input())
answer = 0
start, end = 0, k
while start <= end:
    temp = 0
    mid = (start + end) // 2
    for i in range(1, n+1):
        temp += min(mid//i, n)
    if temp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

# 7보다 작은 수는 몇개인가
#
