import re


s = input()

s_pattern = r"^^PP2.*midterm$"
if re.match(s_pattern, s):
    print("YES")
else:
    print("NO")
