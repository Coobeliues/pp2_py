n = int(input())
for i in range(n):
    a = input().split()
    b = input().split()

    a = set(sorted(a))
    b = set(sorted(b))

    print("Absent:", *sorted(a.difference(b)))
    print("Lost:", *sorted(b.difference(a)))
