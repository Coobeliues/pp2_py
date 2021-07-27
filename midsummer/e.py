n = int(input())
d = {}
ant, bnt, cnt = 0, 0, 0
for i in range(n):
    a, b, c = input().split()

    for j in range(len(a)):
        if 'A' <= a[j] <= 'Z':
            ant += 1
    for j in range(len(b)):
        if b[j] == 'a' or b[j] == 'e' or b[j] == 'o' or b[j] == 'i' or b[j] == 'u' or b[j] == 'y' or b[j] == 'A' or b[j] == 'E' \
                or b[j] == 'O' or b[j] == 'I' or b[j] == 'U' or b[j] == 'Y':
            bnt += 1
    for j in range(len(c)):
        if '0' <= c[j] <= '9':
            cnt += 1
    # d['a'] = d.get('a', 0) + ant
    # d['b'] = d.get('b', 0) + bnt
    # d['c'] = d.get('c', 0) + cnt

d = {'a': ant, 'b': bnt, 'c': cnt}
print(d.items())
