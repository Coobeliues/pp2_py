import math
s=input()
l=len(s)
lel=math.ceil(l/2)
print(s[lel:],s[:lel],sep="")

