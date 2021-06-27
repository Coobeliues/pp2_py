# def power(a,n):
#     res=1
#     if n==0: return res
#     if n<0: return 1/(power(a,-n-1)*a)
#     else: return power(a,n-1)*a
#
# a=int(input())
# n=int(input())
# print(power(a,n))
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(float(input()), int(input())))