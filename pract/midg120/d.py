f = open('i.txt', 'r')
file = f.read().split('\n')
a = []
s = set()

for i in file:
    a.append(i)
for i in range(len(a)):
    s.add(a[i])
s = list(s)

for i in range(len(s)):
    cnt = 0
    for j in range(len(a)):
        if s[i] == a[j]:
            cnt += 1
    if cnt % 2 == 0:
        print(s[i])

# Ayana
# Ayana
# Dias
# Dias
# Dias
# Alik
# Alik
# Alik
# Alik