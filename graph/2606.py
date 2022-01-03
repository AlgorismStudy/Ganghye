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
print(graph)

q = deque()
q.append(1)
visited = [False] * (N + 1)
while q:
    curr = q.popleft()
    if curr not in graph.keys():
        continue
    for i in graph[curr]:
        if not visited[curr]:
            q.append(graph[curr].pop())
            visited[i] = True
print(graph)
print(visited)
