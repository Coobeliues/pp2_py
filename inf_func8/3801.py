a=int(input())
b=int(input())

def rec(a,b):
    if a==0: return b
    return rec(a-1, b+1)

print(rec(a,b))