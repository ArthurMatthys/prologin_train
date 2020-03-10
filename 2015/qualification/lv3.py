import cmath
import math

r = [int(e) for e in input().split(' ')]
nbr = int(input())
out = []
points = []

def norm(a):
    return (a[0] ** 2 + a[1] ** 2) ** (1/2)

for i in range(nbr):
    x, y = [int(e) for e in input().split(' ')]
    points.append(f"{x} {y}")
    x -= r[0]
    y -= r[1]
    if y == 0 and x < 0:
        out.append(math.pi)
    else:
        tmp = cmath.phase(complex(x, y))
        out.append(tmp)

res = []
for i in out[1:]:
    an = i - out[0]
    if an < 0:
        an += 2 * math.pi
    res.append(an)

#print(out)
#print(res)
print(points[res.index(min(res)) + 1])
