from collections import deque

N = int(input())
line_N = int(input())
graph = dict()

for i in range(line_N):
    a, b = map(int, input().split())
    if a not in list(graph):
        graph[a] = [b]
    else:
        graph[a] += [b]

    if b not in list(graph):
        graph[b] = [a]
    else:
        graph[b] += [a]


q = deque()
visited = [False] * (N + 1)
q.append(1)

while q:
    curr = q.popleft()
    if graph[curr]:
        for i in graph[curr]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

print(visited.count(True) - 1)
