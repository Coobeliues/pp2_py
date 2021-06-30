s, x, y = list(), list(), list()
n = 8
for i in range(n):
    b = list(map(int, input().split()))
    l, r = b[0], b[1]
    s.append(l + r)
    x.append(l)
    y.append(r)
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j] or x[i] == x[j] or y[i] == y[j]:
            print("YES")
            exit()
print("NO")