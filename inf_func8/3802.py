def fib(n, c=0, p=1):  # Обычная рекурсия
    if (n == 0): return c
    return fib(n - 1, c + p, c)
print(fib(int(input())))


# def fib(n):
#     if n == 1 or n == 2: return 1
#         return fib(n - 1) + fib(n - 2)
# print(fib(int(input())))