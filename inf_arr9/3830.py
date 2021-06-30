l = list(input().split(' '))
cnt=0
for i in range(len(l)):
    if int(l[i])>0: cnt+=1
print(cnt)