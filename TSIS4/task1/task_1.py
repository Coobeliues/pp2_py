import re

file = open('input.txt', mode='r', encoding="utf8")

text = file.read()

CompanyText = re.findall(r"Филиал.*(\b[A-Z]+)", text)
BINText = re.findall(r"БИН\s(\b\d+)", text)
print(*CompanyText)
print(*BINText)

pro_all = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}"
compiled_toIter = re.compile(pro_all)
for i in re.finditer(compiled_toIter, text):
    print(i.group('name') + '\n' + ' ' + i.group('count') + '\n' + i.group('price') + '\n' + i.group('total1'))

Time_pattern = r"\nВремя: (?P<time>\b\d.*)\n{1}(?P<add>.*)"
Time_text = re.search(Time_pattern, text).group('time')
Add_text = re.search(Time_pattern, text).group('add')

print(Time_text)
print(Add_text)
