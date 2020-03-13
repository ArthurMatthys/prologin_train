size = int(input())

pyramid = []

for _ in range(size):
    pyramid.append([int(e) for e in input().split(' ')])

timing = []
for i, tab in enumerate(pyramid):
    new_tab = []
    for j, time in enumerate(tab):
        if i == 0:
            new_tab.append(time)
        else:
            if j == 0:
                new_tab.append(timing[-1][j] + time)
            elif j < i:
                new_tab.append(min(timing[-1][j], timing[-1][j-1]) + time)
            else:
                new_tab.append(timing[-1][j-1] + time)
    timing.append(new_tab)
print(max(timing[-1]))


