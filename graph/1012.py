from collections import deque

T = int(input())

M, N, K = map(int, input().split())

graph = []

for _ in range(K):
    a, b = map(int, input().split())
    graph.append((a, b))

print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
