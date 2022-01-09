N = int(input())


def dfs(v, visited, d):
    visited.append(v)
    for i in d[v]:
        if i not in visited:
            dfs(i, visited, d)
    return len(visited)


for _ in range(N):
    M = int(input())
    d = dict()

    for _ in range(M):
        per1, per2 = input().split()
        if per1 not in d:
            d[per1] = [per2]
            d[per2] = [per1]
        else:
            d[per1] += [per2]
            d[per2] += [per1]

        print(d)
        visited = []
        # print(dfs(per1, visited, d))
