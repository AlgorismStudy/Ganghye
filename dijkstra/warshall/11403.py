n = int(input())

adj = []
visited = [0 for _ in range(n)]
# graph = {}


def dfs(v):
    for i in range(n):
        if adj[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(v)


for i in range(n):
    arr = list(map(int, input().split()))
    adj.append(arr)
#     for j in range(n):
#         if arr[j] == 1:
#             if i in graph:
#                 graph[i] += [j+1]
#             else:
#                 graph[i] = [j+1]
# print(graph)


for x in range(n):
    dfs(x)
    for y in range(n):
        if visited[y] == 1:
            print(1, end='')
        else:
            print(0, end='')
    print()
    visited = [0 for i in range(n)]
