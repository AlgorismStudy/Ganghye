a, b, c = map(int, input().split())  # a 고정비용 b 가변비용 c 노트북가격

if b >= c:
    print(-1)
else:
    profit = a // (c-b) + 1
    print(profit)
