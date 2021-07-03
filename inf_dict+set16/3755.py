n = int(input())
allnum = set(range(1, n+1))
res = allnum
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(i) for i in guess.split()}
    ans = input()
    if ans == 'YES':
        res &= guess
    else:
        res &= allnum - guess
print(' '.join([str(x) for x in sorted(res)]))
#print(*sorted(res), end=' ')

