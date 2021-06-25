n=int(input())
f=0
s=1
c,twm,res=0,0,0
if n==1:
    print(1)
    exit()
while twm<n-1:
    c=f+s
    f=s
    s=c
    res=s
    twm+=1
print(res)