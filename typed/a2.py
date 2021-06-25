i=int(input())
j=int(input())
if i<j:
    for x in range(i, j+1):
        print(x)
else:
    for x in range(-i, -j+1): print(-x)
