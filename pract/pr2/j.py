def power1(n):
    if n < 2:
        return False
    for prime in range(2, n):
        if n % prime == 0:
            return False

    return True


a, b = input().split()
s = []

for i in range(int(a), int(b)):
    if power1(i):
        s.append(i)

print(*reversed(s))
