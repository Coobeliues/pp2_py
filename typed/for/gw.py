x=int(input())
p=int(input())
y=int(input())
p=p/100+1
cnt=0
while x<y:
    x*=p
    x=int(100*x)/100
    cnt += 1
print(cnt)