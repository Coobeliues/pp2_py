#print(*sorted(map(int, input().split()), key=lambda x: not x))
## ne panimauuu


# lel = list(map(int, input().split()))
# print([i for i in lel if i] + [0]*lel.count(0))
# ne panimauuu

l = list(map(int, input().split()))
l.sort(key=lambda x: not x)
for i in range(len(l)):
    print(l[i], end=" ")


# lst = list(map(int, input().split()))
# for i in reversed(range(len(lst))):
#     if lst[i] == 0:
#         lst.append(lst.pop(i))
# print(*lst)
# ne panimauuu
