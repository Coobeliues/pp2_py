from math import sqrt
def mine(x1, y1, x2, y2):
    c=sqrt((x1-y1)**2 + (x2-y2)**2)
    print(c)
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
mine(x1, x2,y1, y2)
