import re
txt = "Ernar 18 , Narsyhov 2003" \
      "87782938111k@gmail.com, 11.02" \
      "Programmer is  the best" \
      "Ernar is hot boy " \
      "1102 87029922857"
'''
\d - any digit
    [0-9] = 1 => [0-9]{3} = 3
\D - any none digit
\w - alphabet [a-z, A-Z]
\W - any none alph
\s - space or " "
\S - none space
r'[A-Z][a-z]+'
'''
tlukfr = r'\w+@\w+\.\w+'
res = re.findall(tlukfr, txt)
print(res)
