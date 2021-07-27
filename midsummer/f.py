import re

u = input()
p = input()

if len(u) < 7 or len(u) > 36:
    print('Invalid password or username')
    exit()

u_pattern = r"^[A-Za-z0-9._-]{3,32}\#\d{4}$"
p_pattern = r"^[A-Za-z0-9\W]{8,}$"

if re.findall(u_pattern, u) and re.findall(p_pattern, p):
    print('Welcome to Discord')
else:
    print('Invalid password or username')

