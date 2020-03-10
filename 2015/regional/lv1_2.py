input()
temp = [int(e) for e in input().split(' ')]

tmp = [temp[0]]
for index, i in enumerate(temp[1:]):
    tmp.append(i-temp[index])

for i in tmp:
    print(f"{i} ", end="")
