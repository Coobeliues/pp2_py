s = input()

d = {}
a = []
for i in range(len(s)):
    d[s[i]] = d.get(s[i], 0) + 1
print(len(d))
for i, j in enumerate(d.items()):
    print(*j)

