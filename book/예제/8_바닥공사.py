n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[n])

# 헷갈리는부분: d[i-2]*3 이아니고 d[i-2]*2인 이유
