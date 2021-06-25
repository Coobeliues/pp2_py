n=int(input())
f=0
s=1
flag=0
c,twm,res=0,0,0
if n==0:
    print(0)
    exit()
elif n==1:
    print(1)
    exit()
while res<=n:
    c=f+s
    f=s
    s=c
    res=s
    twm+=1
    if res==n:
        flag=1

if flag==0:
    print(-1)
else:
    print(twm)