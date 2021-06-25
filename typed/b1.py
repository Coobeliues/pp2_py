n=20
def factoriallity(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
print(factoriallity(n))

from math import factorial
print(factorial(n))

def facto(n, total=1):
    while True:
        if n == 1:
            return total
        n, total = n - 1, total * n
print(facto(n))

def factori(n):
    if n < 2:
        return 1
    return n * factori(n - 1)
print(factori(n))