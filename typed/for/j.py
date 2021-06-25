n=int(input())
c=0
for x in range(2,n+1):
    c+=(x-1)*x
    # print(x-1,'*',x,'+',sep="", end="")
    # print(x-1, end="")
    # print('*', end="")
    # print(x, end="")
    # print('+', end="")
    print(str(x-1)+'*'+str(x)+'+',end="")
# print(c)