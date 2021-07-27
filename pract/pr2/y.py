def convert(n):
    ans = []
    if n == 0:
        print(0)
        exit()
    while n > 0:
        ans.append(n % 7)
        n //= 7
    print(*reversed(ans), sep='', end='')


convert(int(input()))
