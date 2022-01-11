# 예제만 정답
import math

x, y = map(int, input().split())
z = math.floor((y / x) * 100)

left = 0
right = 100000000000000
if z == 100:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        score = math.floor(((y + mid) / (x + mid)) * 100)
        if score != z:  # 승률이 오르면 더 작은 수가 있는지 찾는다.
            right = mid - 1
        else:  # 승률이 오르지않으면 더 큰 수를 찾는다.
            left = mid + 1
    print(left)
