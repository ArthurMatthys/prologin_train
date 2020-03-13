n = int(input())

group = [int(e) for e in input().split()]

links = [set() for _ in range(n)]

for i, value in enumerate(group):
    links[i].add(value)
    links[value].add(i)

nbr = 0

def remove_elem(elem, links, add=False):
    for i, tab in enumerate(links):
        if elem in tab:
            links[i].remove(elem)
            if add and links[i] == set([]):
                links[i] = set([-1])

while sum([len(i) for i in links]):
    l = [len(i) if i != set([]) else float('inf') for i in links]
    a = l.index(min(l))
    nbr += 1
    remove_elem(a, links)
    cpy = set(links[a])
    for i in cpy:
        if links[i] != set([]) and links[i] != set([-1]):
            links[i] = set([])
            remove_elem(i, links, True)
    links[a] = set([])
    free = len(list(filter(lambda e: e == set([-1]), links)))
    nbr += free
    links = list(map(lambda e: set([]) if e == set([-1]) else e, links))

print(nbr)
