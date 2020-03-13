nbr, size = [int(e) for e in input().split(' ')]

first = []
second = []

for _ in range(nbr):
    first.append([int(e) for e in input().split(' ')])
for _ in range(nbr):
    second.append([int(e) for e in input().split(' ')])



def get_fastest(lst):
    time = []
    for i in lst:
        if i[1] == 0:
            time.append(float('inf'))
            continue
        time.append((size - i[0]) / i[1])
    return time.index(min(time))


def run(first, second):
    i1 = 0
    i2 = 0
    while 1:
        if len(first) == 0:
            print(2 * nbr - len(second) + 1)
            break
        if len(second) == 0:
            print(nbr - len(first) + 1)
            break
        x1, v1 = first[0]
        x2, v2 = second[0]
        if v2 == 0:
            second.pop(0)
            i2 += 1
            continue
        elif v1 == 0:
            first.pop(0)
            i1 += 1
            continue
        else:
            t1 = x2 / v1
            t2 = x1 / v2
            if t1 <= t2:
                second.pop(0)
                i2 += 1
                continue
            else:
                first.pop(0)
                i1 += 1
                continue

run(first, second)
