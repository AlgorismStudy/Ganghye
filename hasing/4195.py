N = int(input())


def dfs(v, visited, d):
    cnt = 1
    visited[v] = True
    for i in d[v]:
        if not visited[i]:
            cnt += 1
            dfs(i, visited, d)
    return cnt


for _ in range(N):
    M = int(input())
    d = dict()

    for _ in range(M):
        per1, per2 = input().split()
        if per1 in d:
            d[per1] += [per2]
        else:
            d[per1] = [per2]

        visited = [False] * len()
        print(dfs(per1, visited, d))
