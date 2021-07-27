n = input().split()
d = 0
r = -1
for i in range(int(n[0])):
    sum = 0

    m = input().split()
    for j in range(len(m)):
        sum += int(m[j])
    if d < sum:
        d = sum
        r = i

print(r+1)
