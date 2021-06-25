n=int(input())
if n==1:
    print("YES")
    exit()
elif n%2==1:
    print("NO")
    exit()
else:
    i = 0
    while i<=n:
        if 2**i == n:
            print("YES")
            exit()
        else:i += 1
print("NO")