# a = [int(i) for i in input().split()]
# d = 0
# ret = 0
# for i in range(len(a)):
#     x = 0
#     cnt = 0
#     for j in range(i+1, len(a)):
#         if a[i] == a[j]:
#             cnt += 1
#             x = a[i]
#     if cnt > ret:
#         d = x
#     ret = cnt
# print(d)
# пашти работает

lazy = [int(i) for i in input().split()]
print(max(lazy, key=lazy.count))
# bestest


# lst = [int(i) for i in input().split()]
# chicken = dict()
# for num in lst:
#    if num in chicken:
#        chicken[num] += 1
#    else:
#        chicken[num] = 1
# print(max(chicken.items(), key=lambda x: x[1])[0])
