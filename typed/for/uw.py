current=-123
result = 0
last = 123
while current!=0:
    if (last, current := int(input())) == (current, last,):
        result += 1
        last = current

print(result)

