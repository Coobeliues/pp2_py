prev=-123
maxorigin=0
maxi=0
x=int(input())
while x!=0:
    if prev==x:
        maxi+=1
    else:
        prev=x
        maxorigin=max(maxi, maxorigin)
        maxi=1
    x=int(input())
maxorigin=max(maxi, maxorigin)
print(maxorigin)