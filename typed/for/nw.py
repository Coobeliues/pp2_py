x=-1
first=-111
second=-111
while x!=0:
    x=int(input())
    if x>first:
        second=first
        first=x
    elif x>second and second!=first:
        second=x
print(second)