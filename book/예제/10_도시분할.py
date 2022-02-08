import sys


def find(parent, a):
    if a != parent[a]:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
parent = [i for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph = sorted(graph, key=lambda x: x[2])
result = 0
last = 0

for a, b, c in graph:
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        union(parent, a, b)
        result += c
        last = c
print(result - last)
