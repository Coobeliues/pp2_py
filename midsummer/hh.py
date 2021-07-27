import re

inp = input()
nik, dom, su = [], [], []

email = re.findall(r"[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}", inp)
email.sort()

for i in email:
    nik.append(i.split('@')[0])
    dom.append(i.split('@')[1].split('.'))
    su.append(i.split('@')[1].split('.')[1])

print('nicknames:')
print(*nik)

print('domain name:')
for i in dom:
    print(i[0], end=' ')
print()
# print(*dom)

print('suffix:')
print(*su)


# 12_@12w2.qw qwe@qwe.qwe,also@a.mail
# mail@ma.il,sprtd@by.sym.also@mail.ru
# asman_5@mail.ru _kymbat@gmail.com
