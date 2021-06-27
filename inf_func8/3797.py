import math
def reduce_fraction(n,m):
    k = math.gcd(n,m)
    print (n//k, m//k)
reduce_fraction(int(input()), int(input()))