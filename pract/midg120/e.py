d = dict()
for i in range(int(input())):
    l = input().split()
    d[l[0]] = [l[i] for i in range(2, len(l))]

for i in range(int(input())):
    found = False
    city = input()
    for key, value in d.items():
        if city in value:
            found = True
            print(key)
    if not found:
        print('Unknown')
