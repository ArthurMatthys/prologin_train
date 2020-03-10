import math
nbr = int(input())
length = int(input())
speed = [int(e) for e in input().split()]
start = [int(e) for e in input().split()]

times = []
for index, i in enumerate(speed):
    s = start[index]
    new_dist = length - s
    if new_dist <= 0:
        times.append(0)
    else:
        times.append(math.ceil(new_dist/i))

print(times.index(min(times)))
