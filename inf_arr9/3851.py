a = list(map(int, input().split()))
N, k = a[0], a[1]
c = list("I" * N)

for i in range(k):
    b = list(map(int, input().split()))
    l, r = b[0], b[1]
    for x in range(l-1, r):
        c[x] = '.'
print("".join(c))

