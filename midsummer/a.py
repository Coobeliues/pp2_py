a = [str(i) for i in input().split()]
cnt = 0
for i in range(len(a)):
    if len(a[i]) % 2 == 0:
        cnt += 1
print(cnt)
