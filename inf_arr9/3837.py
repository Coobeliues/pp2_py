a = [int(i) for i in input().split()]
x = int(input())
r = -1
for i in range(len(a)):
    if a[i] >= x:
        r = i
print(r+2)
