n, k = input().split()
cnt = 0
for i in range(int(n)):
    sumi = 0
    x, y, z = input().split()
    sumi += int(x) + int(y) + int(z)
    if sumi >= int(k):
        cnt += 1
if cnt != 0:
    print('YES')
else:
    print('NO')