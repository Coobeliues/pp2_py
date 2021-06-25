maximum = -1111
num_maximal = 0
element = 123
while element != 0:
    element = int(input())
    if element > maximum:
        maximum=element
        num_maximal=1
    elif element == maximum:
        num_maximal += 1
print(num_maximal)