import re

s = input()
s_pattern = r"[A-Z]{1}[a-z]+"
if re.findall(s_pattern, s):
    print('YES')
else:
    print("NO")
