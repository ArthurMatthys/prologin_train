import heapq

N, M, R = [int(e) for e in input().split(' ')]
adj = [[float('inf') for _ in range(N)] for _ in range(N)]

paths = [{} for _ in range(N)]
for _ in range(M):
    x, y, l = [int(e) for e in input().split(' ')]
    paths[x-1][y-1] = l

def dji(start):
    h = [(0, start)]
    while len(h):
        size, node = heapq.heappop(h)
        for (new_node, weight) in paths[node].items():
            if size + weight < adj[start][new_node]:
                adj[start][new_node] = size + weight
                heapq.heappush(h, (size + weight, new_node))


for _ in range(R):
    start, end = map(int, input().split(' '))
    if adj[start - 1][end - 1] == float('inf'):
        dji(start - 1)
    print(adj[start - 1][end - 1])

