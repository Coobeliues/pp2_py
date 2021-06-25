n=int(input())
for x in range(n):
    print("+___",sep="", end=" ")
print()
for x in range(1,n+1):
    print("|",x," / ",sep="", end="")
print()
for x in range(n):
    print("|__\\", sep="",end=" ")
print()
for x in range(n):
    print("|   ", sep="",end=" ")
print()
