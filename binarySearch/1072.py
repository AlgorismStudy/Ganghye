# 예제만 정답
x, y = map(int, input().split())
z = y * 100 // x
# z = (y/x) * 100

left = 0
right = x

if z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        score = (y + mid) * 100 // (x + mid)
        if score > z:  # 승률이 오르면 더 작은 수가 있는지 찾는다.
            right = mid - 1
        else:  # 승률이 오르지않으면 더 큰 수를 찾는다.
            left = mid + 1
    print(left)
