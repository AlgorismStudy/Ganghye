def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v = int(input())
e = int(input())
arr = []
parent = [0] * (v+1)
result = 0
graph = [(0, 0)] * (v+1)

for _ in range(e):
    x, y, w = map(int, input().split())
    arr.append((x, y, w))

arr = sorted(arr, key=lambda x: x[2])


for i in range(1, v+1):
    parent[i] = i

for x, y, w in arr:
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        union_parent(x, y)
        result += w
print(result)
