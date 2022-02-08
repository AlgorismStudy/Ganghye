v, e = map(int, input().split())
arr = []

for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))

arr.sort()


def find(parent, a):
    if a != parent[a]:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


parent = [i for i in range(v+1)]
result = 0

for c, a, b in arr:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
print(result)
