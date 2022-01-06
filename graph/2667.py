from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]


def bfs(graph, v, visited):
    q = deque([v])
    visited[v[0]][v[1]] = True
    count = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return count


l = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            temp = [i, j]
            l.append(bfs(graph, temp, visited))

print(len(l), *sorted(l), sep="\n")
