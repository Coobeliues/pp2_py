def primera(n):
    for i in range(1, int(n**0.5)+1 ,2):
        if i==1: continue
        if n%i==0: return False
    return True

n=int(input())
if n % 2 == 0 and n>2:
    print("NO")
    exit()
elif n<2:
    print("NO")
    exit()
if primera(n)==False: print("NO")
else: print("YES")

#nice