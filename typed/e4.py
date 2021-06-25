# s=input()
# a=s.find('f')
# b=s.rfind('f')
# if a==-1: print()
# elif a==b: print(a)
# else: print(a, b)

#!/usr/bin/env python3

# s = input()
# count = len(s) - len(s.replace('f', ''))
# if count == 0:
#     pass
# elif count == 1:
#     print(s.index('f'))
# else: # count > 1
#     print(s.index('f'), s.rindex('f'))
s=input()
try:
    i = s.index('f')
except ValueError:  # count == 0
    pass
else:
    try:
        j = s.rindex('f', i+1)
    except ValueError:  # count == 1
        print(i)
    else:               # count > 1
        print(i, j)