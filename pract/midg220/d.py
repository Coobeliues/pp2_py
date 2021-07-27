s = input()
n, m = input().split()
x = y = 0
flag = False
for i in range(len(s)):
    if s[i] == 'D':
        y -= 1
    elif s[i] == 'U':
        y += 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'L':
        x -= 1
    if x == int(n) and y == int(m):
        flag = True
if flag:
    print(1)
else:
    print(0)
