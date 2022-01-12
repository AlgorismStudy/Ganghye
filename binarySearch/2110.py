import sys

n, c = map(int, sys.stdin.readline().split())
home = []

for i in range(n):
    home.append(int(sys.stdin.readline()))
home.sort()


start, end = 0, max(home)
max_d = 0

while start <= end:
    d = 0
    mid = (start + end) // 2
    wifi = [0]
    for i in range(1, n):
        d += home[i] - home[i - 1]
        if d >= mid:
            wifi.append(i)
            d = 0
    if len(wifi) >= c:  # 공유기 숫자를 초과했으면 더 늘려도 됨
        if mid > max_d:
            max_d = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_d)
