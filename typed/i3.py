p=float(input())
r=float(input())
k=float(input())
y=int(input())
p=p/100+1
k=k%100
rk=k+r
for i in range(y):
    rk=round(rk*p,10)
print(int(rk), int((rk-int(rk))*100), sep=" ")

