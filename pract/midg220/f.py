n, k = [int(i) for i in input().split()]
cnt = 0
while n <= k:
    n *= 3
    k *= 2
    cnt += 1

print(cnt)
