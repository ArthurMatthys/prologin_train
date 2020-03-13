n = int(input())

adj = [[] for _ in range(n)]
times = [-1 for _ in range(n)]
for i in range(n):
    a = [int(e) for e in input().split(' ')]
    if a[0] == 0:
        continue
    index = 1
    while index < len(a):
        adj[i].append((a[index], a[index+1]))
        index += 2


def calc_rec(adj, times, i):
    if times[i] != -1:
        return times[i]
    if adj[i] == []:
        return 0
    a = 0
    for j in adj[i]:
        a = max(a, calc_rec(adj, times, j[0]) + j[1])
    times[i] = a
    return a

for i in range(n):
    calc_rec(adj, times, i)

print(max(times))
