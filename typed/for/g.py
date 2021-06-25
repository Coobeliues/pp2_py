n=int(input())
k=int(input())
nn=1
kk=1
nk=1
for x in range(1,n+1):
    nn=nn*x
for x in range(1,k+1):
    kk=kk*x
for x in range(1,n-k+1):
    nk=nk*x
print(nn//(nk*kk))