a = [int(i) for i in input().split()]
n = int(input())
b = []
for i in range(1, a[-1]):
    b.append(i)
a, b = set(a), set(b)
b = b.difference(a)
b = list(b)
for i in range(len(b)):
    if n - 1 == i:
        print(b[i])
        exit()