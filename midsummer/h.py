import re

a = [str(i) for i in input().split()]
look_for = r"\w+[\w.'+-]+@[^\W_]+[.-][A-Za-z0-9.-]+\w"
nick = r"^\w+[\w.'+-]+"
domain = r"\@\w+"
suff = r"\w+[\w'+-]+$"

ni, do, su = [], [], []

print('nicknames:')
for i in range(len(a)):
    ni.append(*sorted(re.findall(nick, a[i])))
    # print(*sorted(re.findall(nick, a[i])), end=' ')
print(*sorted(ni))

print('domain name:')
for i in range(len(a)):
    do.append(*sorted(re.findall(domain, a[i])))
    # print(*sorted(re.findall(domain, a[i])), end=' ')
for i in range(len(do)):
    for j in range(len(do[i])):
        if do[i][j] != '@':
            print(do[i][j], end='')
    print(end=' ')
print(end='\n')

print('suffix:')
for i in range(len(a)):
    su.append(*sorted(re.findall(suff, a[i])))
    # print(*reversed(re.findall(suff, a[i])), end=' ')
print(*sorted(su))
