a = [int(i) for i in input().split()]
k = int(input())
a.pop(k)
for i in range(len(a)):
    print(a[i], end=" ")
