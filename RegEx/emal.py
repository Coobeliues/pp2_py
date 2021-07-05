import re

file_n = "i.txt"
txt_file = 'o.txt'
input_f = open(file_n, mode='r', encoding='Latin-1')
output_f = open(txt_file, mode='w', encoding='Latin-1')

mine = input_f.read()

look_for = r"\w+[\w.'+-]+@[^\W_]+[.-][A-Za-z0-9.-]+\w"

res = re.findall(look_for, mine)

for i in res:
    print(i)
    output_f.write(i + '\n')
print(len(res))

