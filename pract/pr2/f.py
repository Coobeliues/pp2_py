import math


def log2(x): return math.log10(x) / math.log10(2)


def power1(n): return math.ceil(log2(n)) == math.floor(log2(n))


a = list({int(i) for i in input().split()})

for i in a:
    if not power1(i):
        print(i, end=' ')
