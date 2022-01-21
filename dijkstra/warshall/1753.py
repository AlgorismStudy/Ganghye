import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
INF = int(1e9)

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while(q):
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
