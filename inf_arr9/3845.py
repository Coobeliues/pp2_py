a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.insert(b[0], b[1])
for i in range(len(a)):
    print(a[i], end=" ")
