n = int(input())

group = [int(e) for e in input().split()]

def dp(lst, eat, group, index):
    if index == n:
        return len(lst)
    if group[index] in lst:
        return dp(lst, eat, group, index+1)
    if index in eat:
        return dp(lst, eat ,group, index+1)
    else:
        return max(dp(lst + [index], eat + [group[index]], group, index + 1), dp(lst, eat, group, index+1))


a = dp([], [], group, 0)
print(a)

