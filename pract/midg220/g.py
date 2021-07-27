import re

a = input()
b = input()
c = input()
d = input()

a = a.replace(b, c)

print(len(re.findall(d, a)))
