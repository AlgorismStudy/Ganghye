n, m = map(int, input().split())

l = list(map(int, input().split()))

start = 0
end = max(l)
result = 0
while start <= end:
    mid = (start + end) // 2
    answer = 0
    for i in l:
        if i > mid:
            answer += i - mid
    if answer < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
