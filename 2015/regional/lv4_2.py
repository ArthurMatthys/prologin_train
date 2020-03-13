h, l = [int(e) for e in input().split(' ')]

height = dict()
mount = [list(map(int, input().split(' '))) for _ in range(h)]

for i in mount:
    for e in i:
        height[e] = 0

dd = [[1,0],[-1,0],[0,1],[0,-1]]

def flood(mount, dic, x, y):
    new_h = mount[x][y]
    mount[x][y] = -1
    nbr = 0
    heap = [(x, y)]
    while len(heap):
        xx, xy = heap.pop()
        nbr += 1
        for d in dd:
            dx = d[0]
            dy = d[1]
            new_x = xx + dx
            new_y = xy + dy
            if 0 <= new_x < h and 0 <= new_y < l and mount[new_x][new_y] == new_h:
                mount[new_x][new_y] = -1
                heap.append((new_x, new_y))

    if dic[new_h] < nbr:
        dic[new_h] = nbr

for i in range(h):
    for j in range(l):
        if mount[i][j] != -1:
            flood(mount, height, i, j)
print(max(height.values()))
