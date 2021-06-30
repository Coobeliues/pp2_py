a = [int(i) for i in input().split()]
sor = sorted(a)
for i in range(len(sor)):
    if sor[i] % 2 == 1:
        print(sor[i])
        exit()
print(0)
