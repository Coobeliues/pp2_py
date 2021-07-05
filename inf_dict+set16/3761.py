d = {}
with open('input.txt', 'r') as file:
    for line in file:
        word, k = line.split()
        d[word] = d.get(word, 0) + int(k)
for i, j in sorted(d.items()):
    print(i, j)
