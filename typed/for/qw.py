result = 0
last = 123
while (last, current := int(input())) != (0, 0,):
    result += current
    last = current
print(result)