numbers = [int(i) for i in input().split()]
occur_before = set()
for i in numbers:
    if i in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(i)
