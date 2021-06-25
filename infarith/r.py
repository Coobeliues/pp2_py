a = int(input())
b = int(input())
# print((a+b- abs(a-b))//2 +abs(a-b))
print(
    a * (1 % (a // b + 1)) +
    b * (1 % (b // a + 1)) *
    (1 % ((int((a * b) - a ** 2) + 1)))
)