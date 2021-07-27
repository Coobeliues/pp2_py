n = int(input())
d = set()
c = set()
a = list(str(i) for i in input().split())
m = int(input())
b = list(str(i) for i in input().split())
for i in range(n):
    d.add(a[i])
for i in range(m):
    c.add(b[i])

both = c.intersection(d)
ans1 = list(d - both)
ans2 = list(c - both)
print(*ans1, *ans2, sep='\n')
# print(list((d - both)), sep='\n')
# print(list(c - both), sep='\n')
