n = int(input())

time = []
profit = []
for i in range(n):
    a, b = map(int, input().split())
    time.append(a)
    profit.append(b)

d = [0] * (n+1)
max_sum = 0
for i in range(n-1, -1, -1):
    if time[i] + i - n <= 0:  # 상담가능한 time이라면
        d[i] = max(profit[i] + d[time[i]+i], max_sum)  # 현재일 맡기 vs 맡지않기
        max_sum = d[i]
    else:
        d[i] = max_sum
print(d[0])
