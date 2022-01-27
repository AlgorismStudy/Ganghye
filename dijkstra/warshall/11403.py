def dfs(v):
    for i in range(n):
        if adj[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


n = int(input())

adj = []
visited = [0 for _ in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))
    adj.append(arr)


for i in range(n):
    dfs(i)
    print(*visited)
    visited = [0 for _ in range(n)]


# 플로이드-워셜
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = max(graph[i][k]*graph[k][j], graph[i][j])
