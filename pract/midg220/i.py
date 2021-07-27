n = int(input())
a = [int(i) for i in input().split()]
k = int(input())
s = ''
t = ''
for i in range(k):
    s += str(a[i])
for i in range(k,len(a)):
    t += str(a[i])
print(int(s) * int(t))