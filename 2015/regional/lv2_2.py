def crenau(nbr, h):
    tot = 0
    for _ in range(nbr-1):
        print("           _  ", end="")
        tot += 4
    print(" _ ")
    tot += 3
    for _ in range(nbr - 1):
        print("| |_", end="")
    print("| |")
    
    for _ in range(h-2):
        print("|", end="")
        for _ in range(tot - 2):
            print(" ", end="")
        print("|")
    
    print("|", end="")
    for _ in range(tot - 2):
        print("_", end="")
    print("|")

nbr = int(input())
h = int(input())

crenau(nbr, h)
