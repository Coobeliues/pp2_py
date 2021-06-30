a = [int(i) for i in input().split()]
mx = max(a)
mn = min(a)
r=-1
for i in range(len(a)):
    if mn == a[i]:
        a[i] = mx
        r = i
    if mx == a[i] and r != i:
        a[i] = mn
print(' '.join([str(i) for i in a]))
