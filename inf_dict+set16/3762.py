d = {}
maxi = -111111
ans = ''
with open('input.txt', 'r') as file:
    for line in file:
        for word in line.split():
            d[word] = d.get(word, 0) + 1
for i, j in sorted(d.items()):
    if j > maxi:
        maxi = j
        ans = i
print(ans)
