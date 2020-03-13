import heapq

h, l = [int(e) for e in input().split()]

map1 = [list(input()) for _ in range(h)]
map2 = [list(input()) for _ in range(h)]

maps = [map1] + [map2]


def manhattan(start, end):
    return abs(end[1] - start[1]) + abs(end[0] - start[0]) + (start[2] != end[2])

dd = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]

def astar(maps, start, end):
    heap = [(manhattan(start, end), start, 0)]
    heapq.heapify(heap)
    visited = set()
    while len(heap):
        a = heapq.heappop(heap)
        visited.add(a[1])
        dist = a[0]
        pos = a[1]
        path = a[2]
        if pos == end:
            return path
        else:
            for op in dd:
                dx = op[0]
                dy = op[1]
                dz = op[2]
                x = pos[0] + dx
                y = pos[1] + dy
                z = pos[2] + dz
                if (z == 0 or z == 1) and (0 <= x < h) and (0 <= y < l) and ((x,y,z) not in visited):
                    if maps[z][x][y] != '#':
                        heapq.heappush(heap, path + (manhattan((x,y,z), end), (x,y,z), path+1))
    return 0


for i in range(h):
    if 'a' in maps[0][i]:
        end = (i, maps[0][i].index('a'), 0)
    if 'd' in maps[0][i]:
        st = (i, maps[0][i].index('d'), 0)

print(astar(maps, st, end))
