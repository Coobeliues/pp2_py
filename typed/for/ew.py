n=int(input())
k=0
while k<=n:
    if 2**k>=n:
        print(k)
        exit()
    else: k+=1