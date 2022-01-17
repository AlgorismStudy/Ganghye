from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())


def bfs(v, visited):
    q = deque()
    q.append(v)
    while(q):
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny] == 1:
                visited[nx][ny] += 1
                q.append((nx, ny))
    return visited


for i in range(T):
    m, n, k = map(int, input().split())  # 가로 M 세로 N 배추갯수 K
    graph = [[0]*m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    print(bfs((0, 0), graph))
