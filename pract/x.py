sumi = 0
d = {}
dr = {}
for i in range(int(input())):
    s, n = input().split()
    d[s] = d.get(s, 0) + int(n)
    sumi += int(n)
for i, j in d.items():
    res = j/sumi*100
    k = 0
    if res == int(res):
        k = int(res)
    else:
        k = round(res, 4)
    ans = str(k) + '%'
    dr[i] = ans
    # print(i, str(k) + '%')
# print({k: v for k, v in sorted(dr.items(), key=lambda item: item[1])})
# print(sorted(dr.items(), key=lambda item: item[1:]))