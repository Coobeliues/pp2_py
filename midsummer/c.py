a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
k = int(input())
sumi = 0
for i, j in zip(a, b):
    if i <= k <= j:
        sumi += 1
print(sumi)
