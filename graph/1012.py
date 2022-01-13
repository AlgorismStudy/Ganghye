from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())


def bfs(v, visited, graph):
    q = deque()
    q.append(graph[v[1]][v[0]])
    visited[v[1]][v[0]] = True
    while(q):
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            visited[ny][nx] = True
            q.append(graph[ny][nx])
    return visited


for i in range(T):
    m, n, k = map(int, input().split())  # 가로 M 세로 N 배추갯수 K
    graph = [[0]*m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    visited = [[False] * m for _ in range(n)]
    print(bfs((0, 0), visited, graph))
