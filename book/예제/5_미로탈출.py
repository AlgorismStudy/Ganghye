# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
from collections import deque
n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(v, graph):
    q = deque()
    q.append(v)

    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    for i in graph:
        print(i)
    return graph[n-1][m-1]


print(bfs((0, 0), graph))
