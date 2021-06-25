s=input()
f=s.find('h')
f2=s.rfind('h')
newstr=s[:f]
str2=s[f2+1:]
print(newstr+str2)