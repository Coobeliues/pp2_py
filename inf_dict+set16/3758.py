n, k = [int(i) for i in input().split()]
lst = set()

def fun3(lst):
    return set(num for num in lst if num % 7 != 0 and num % 7 != 6)

for i in range(k):
    a, b = [int(j) for j in input().split()]
    sum_r = a
    while sum_r <= n:
        lst.add(sum_r)
        sum_r += b

print(len(fun3(lst)))
