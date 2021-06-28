def perm(n,k,sumn=1,sumk=1,sumnk=1):
    for x in range(2,n+1):
        sumn*=x
    for x in range(2,k+1):
        sumk*=x
    for x in range(2,(n-k)+1):
        sumnk*=x
    return sumn//(sumk*sumnk)
print(perm(int(input()), int(input())))


# from math import factorial
# def perm(n,k):
#     a=factorial(n)
#     b=factorial(k)
#     nk=n-k
#     ab=factorial(nk)
#     return a//(b*ab)
# print(perm(int(input()), int(input())))


# def perm(n,k,x=1):
#     x=n-k
#     if n==0: return 1
#     if k== 0: return 1
#     if x==0: return 1
#
#     return perm(n-1,0,0)*n/(perm(0,k-1,0)*k*perm(0,0,x-1)*x)
# print(perm(int(input()), int(input())))


# def C(n, k):
#     return fact(n) // (fact(k) * fact(n - k))
# def fact(n):
#     tmp = 1
#     while n > 1:
#         tmp *= n
#         n -= 1
#     return tmp
# print(C(int(input()), int(input())))


