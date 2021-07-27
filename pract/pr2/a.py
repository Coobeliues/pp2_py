a, b = input().split()

if int(a) <= 2187 and int(b) >= 6561:
    print(6561, 2187)
elif 2187 < int(a) < 6561 <= int(b):
    print(6561)
elif 6561 > int(b) >= 2187 > int(a):
    print(2187)
else:
    print(0)
