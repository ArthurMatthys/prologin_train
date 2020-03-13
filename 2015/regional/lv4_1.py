h, l = [int(e) for e in input().split(' ')]
x, y = [int(e) for e in input().split(' ')]

plate = [list(map(int, input().split(' '))) for _ in range(h)]

stack = set()
stack.add((x, y))
origin = plate[x][y]
nbr = 0
l_of = [[1,0], [-1,0], [0,1], [0,-1]]
while len(stack):
    ax, ay = stack.pop()
    color = plate[ax][ay]
    for of in l_of:
        if (0 <= ax + of[0] < h) and (0 <= ay + of[1] < l):
            if plate[ax+of[0]][ay+of[1]] == origin:
                stack.add((ax+of[0], ay+of[1]))
                plate[ax+of[0]][ay+of[1]] = 5
            elif plate[ax+of[0]][ay+of[1]] == 2:
                plate[ax+of[0]][ay+of[1]] = 5
                nbr +=1

print(nbr)
