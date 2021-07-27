def powre(sumch):
    pwr = 1
    while sumch != pwr:
        if pwr >= 1000:
            return  False
        pwr *= 2
    else:
        return True


n = int(input())
txt = []
while n > 0:
    txt.append(input())
    n -= 1

cnt = 0
for line in txt:
    for c in enumerate(line):
        if 'a' <= c[1] <= 'z' or 'A' <= c[1] <= 'Z':
            cnt += 1
        if c[1] == ' ' or c[1] == '\n' or c[0] + 1 == len(line):
            if powre(cnt):
                print('H', end=' ')
            else:
                print('C', end=' ')
            cnt = 0
    print()
