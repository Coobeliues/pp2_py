d = {}
a = {}
ans = {}
for i in range(int(input())):
    s, n = input().split()
    d[s] = d.get(s, 0) + int(n)
    a[s] = a.get(s, 0) + 1
for k, v in d.items():
    ans[k] = f'{v / a[k]:3f}'
    # for i, j in a.items():
    #     if k == i:
    #         v /= j
    # ans[k] = f'{v:.3f}'

for i, j in sorted(ans.items(), key=lambda x: x[0] and x[1], reverse=True):
    print(i, ': ', j, sep='', end='\n')
