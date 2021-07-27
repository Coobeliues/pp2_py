d = {}
file = "euioaEUIOA"
for i in range(int(input())):
    ant = bnt = cnt = 0
    a = input().split()

    ant += sum(map(str.isupper, a[0]))

    for k in a[1]:
        for j in file:
            if k == j:
                bnt += 1

    cnt += sum(map(str.isdigit, a[2]))

    d['a'] = d.get('a', 0) + ant
    d['b'] = d.get('b', 0) + bnt
    d['c'] = d.get('c', 0) + cnt

print(d)
