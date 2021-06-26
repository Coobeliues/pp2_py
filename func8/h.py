n=int(input())
m=int(input())
b=min(m,n)
for i in range(2,b):
    if m%i==0 and n%i==0:
        m/=i
        n/=i
        i-=1
print(n, m)