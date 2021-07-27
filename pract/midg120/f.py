import string
n = int(input())
s = input()
d = dict(enumerate(string.ascii_uppercase))
print(''.join([d[(string.ascii_uppercase.index(c) + n) % 26] for c in s]))

