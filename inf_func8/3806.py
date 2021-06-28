def power(a, n):
    if n==0: return 1
    if n%2==0: return power(a*a,n//2)
    else: return power(a, n - 1)*a
    #return (1 if n == 0
            #else power(a * a, n // 2) if n % 2 == 0
            #else a * power(a, n - 1))

print(power(float(input()), float(input())))


