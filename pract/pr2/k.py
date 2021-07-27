import math
def log2(x): return math.log10(x) / math.log10(2)


def power1(n): return math.ceil(log2(n)) == math.floor(log2(n))

def uniq(arr):
    s = []
    count = arr.count
    for x in arr:
        if count(x) == 1:
            if power1(x):
                s.append(x)
    print(*sorted(s))


a = [int(i) for i in input().split()]
uniq(a)
