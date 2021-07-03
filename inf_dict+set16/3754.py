f = open('input.txt', 'r')
words = set()
for i in f:
    words.update(i.split())
print(len(words))
