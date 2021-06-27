def MinDivisor(n):
    if n % 2 == 0:
        print(2)
        exit()
    else:
        for i in range(1, int(n ** 0.5) + 1, 2):
            if i == 1: continue
            if n % i == 0:
                print(i)
                exit()
        print(n)
n=int(input())
MinDivisor(n)
