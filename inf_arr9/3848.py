from collections import Counter
a = [int(i) for i in input().split()]
print(len(Counter(a).keys()))  # equals to list(set(a))
