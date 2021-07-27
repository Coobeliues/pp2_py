# n, words, ans = int(input()), [], []
# for i in range(n):
#     words.append(input())
# for char in words[0]:
#     ok = True
#     for i in range(n):
#         if words[i].find(char) == -1:
#             of = False
#             break
#     if ok:
#         ans.append(char)
# if len(ans) != 0:
#     print(*sorted(set(ans)))
# else:
#     print("NO COMMON CHARS")

lil_pump = []
n = int(input())
for i in range(n):
    s = set(input())
    lil_pump.append(s)
if set.intersection(*lil_pump):
    print(*sorted(set.intersection(*lil_pump)))
else:
    print('NO COMMON CHARACTERS')

