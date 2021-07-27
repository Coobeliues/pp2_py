n = int(input())
a = [int(i) for i in input().split()]
cnt = 1
for i in range(len(a)):
    if i + 1 >= len(a):
        break
    if a[i] <= a[i+1]:
        cnt += 1

print('YES' if cnt == n else 'NO')
