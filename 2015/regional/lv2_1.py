input()
line = input().split(' ')
input()
rem = [int(e) for e in input().split(' ')]

for index, word in enumerate(line):
    if index + 1 in rem:
        for _ in range(len(word)):
            print('*', end="")
    else:
        print(word, end="")
    print(' ', end="")

