N = list(map(int, input().split(" ")))

current = list(map(int, input().split(" ")))
d = current.pop()
graph = []
direction = []

for i in range(N[0]):
    graph.append(input().split(' '))

for i in graph:
    
    