# def reverse():
#     x = int(input())
#     if x != 0:
#         reverse()
#     print(x)
#
# reverse()


def rec():
    n = int(input())
    if n != 0:
        rec()
    print(n)
rec()