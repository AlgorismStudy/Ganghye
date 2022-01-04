import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph[1:]:
    i.sort()

dfs_visited = [False] * (N + 1)
dfs_answer = []


def dfs(graph, v, visited):
    visited[v] = True
    dfs_answer.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


bfs_visited = [False] * (N + 1)
bfs_answer = []


def bfs(graph, v, visited):
    q = deque([v])
    bfs_answer.append(v)
    visited[v] = True
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                bfs_answer.append(i)


dfs(graph, V, dfs_visited)
print(*dfs_answer, sep=" ")

bfs(graph, V, bfs_visited)
print(*bfs_answer, sep=" ")
