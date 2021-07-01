n = int(input())
g, x = map(str, input().split())
l = [x]
q = dict()
w = 1
last = x
lat = g
l.append(g)
while True:
    g, x = map(str, input().split())
    if g not in l:
        l.append(g)

    if last != x:
        q[last] = w
        w = 1
    else:
        w += 1

    if x != lat:
        q[g] = 0

    last = x
    lat = g
    if len(l) == n:
        q[last] = w
        break

print(q)
