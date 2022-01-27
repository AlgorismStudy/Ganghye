import heapq

n, m, k, x = map(int, input().split())
d = [[] for _ in range(n)]

for _ in range(1, m+1):
    x, y = map(int, input().split())
    d[x].append((y, 1))
answer = 0
INF = 1e9
distance = [INF] * (n+1)


def dijkstra(v):
    q = []
    distance[v] = 0
    heapq.heappush(q, (0, v))
    while(q):
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for i in d[node]:
            cost = dist + i[1]


dijkstra(k)
print(distance)
