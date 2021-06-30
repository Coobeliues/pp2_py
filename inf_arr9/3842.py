a = [int(i) for i in input().split()]
a.insert(0, a[len(a)-1])
for i in range(len(a)-1):
    print(a[i], end=" ")
