n = int(input())
a = {int(i) for i in input().split()}
b = list(a)
for i in range(len(a)):
    print(i+1, b[i])
