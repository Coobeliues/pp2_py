h,a,b = map(int,input().split())
ans = 0
cnt = 0
while True:
    ans+=a
    cnt += 1
    if ans>=h:
        break
    ans-=b
print(cnt)
