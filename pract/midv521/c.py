n, k = input().split()
a = [int(i) for i in input().split()]
b = []

for i in range(int(n), int(k)+1):
    b.append(i)

c = list(set(b) - set(a))

print(*c)
