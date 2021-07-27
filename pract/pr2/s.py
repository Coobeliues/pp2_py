n = int(input())
a = [int(i) for i in input().split()]
maxi = -1111111
for i in range(len(a)):
    if a[i] > maxi:
        maxi = a[i]
for i in range(len(a)):
    if a[i] == maxi:
        a[i] = 1
    else:
        a[i] = 0
print(*a)
