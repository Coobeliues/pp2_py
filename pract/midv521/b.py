a = [int(i) for i in input().split()]

print(max(set(a), key=a.count))
