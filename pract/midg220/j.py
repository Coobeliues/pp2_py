import json

f = open('input.txt', 'r')
file = f.read()
data = json.loads(file)
ans, res, mn = 0, '', 9999999

for i in data['Subscriptions']:
    price = int(i['price'])
    dis = int(i['discount'])
    ans = int(price * (100 - dis) / 100)
    if mn > ans:
        mn = ans
        res = str(i['name'])

print('Name: ' + res + '\nPrice: ' + str(mn))
