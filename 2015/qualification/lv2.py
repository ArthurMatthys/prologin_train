a = int(input())
it = int(input())

for i in range(it):
    if a % 2:
        a = a * 3 + 1
    else:
        a /= 2

print(int(a))

