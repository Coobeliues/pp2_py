l = list(input().split(' '))
for i in range(len(l)):
    if i+1>=len(l): break
    if int(l[i])<int(l[i+1]): print(l[i+1],end=" ")