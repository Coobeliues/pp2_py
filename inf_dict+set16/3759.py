d = {}
with open('input.txt', 'r') as file:
    for line in file:
        for word in line.split():
            d[word] = d.get(word, -1) + 1
            print(d[word], end=' ')