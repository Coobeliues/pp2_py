maxi= dec= inc =1
prev=int(input())
while prev:
    maxi=max(inc, dec, maxi)
    x=int(input())
    if prev>x:
        dec, inc= dec+1, 1
    elif prev<x:
        inc, dec=inc+1, 1
    else: inc=dec=1
    prev=x
print(maxi)