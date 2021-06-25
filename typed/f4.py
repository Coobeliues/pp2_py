s=input()
a=s.find('f')
b=s.rfind('f')
c=s[:s.find('f')]
d=s[s.find('f')+1:]
ded=d.find('f')
if a==-1: print(-2)
elif a==b: print(-1)
else: print(ded+len(c)+1)