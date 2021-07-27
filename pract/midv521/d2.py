import math


def Log2(x):
    return (math.log10(x) / math.log10(2))


def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))


for i in range(int(input())):
    s = input()
    s = s.replace(':', '')
    s = s.replace(',', '')
    s = s.replace("’", '')
    s = s.replace('?', '')
    s = s.replace('!', '')
    l = s.split()
    for j in l:
        if isPowerOfTwo(len(j)):
            print('H', end=' ')
        else:
            print('C', end=' ')
