import math

n = int(input())
str_list = []
guns = []
full_ans = []

def Log2(x):
    return (math.log10(x) / math.log10(2))


def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))


for i in range(n):
    str_list.append(input().split())

for i in range(len(str_list)):
    for j in range(len(str_list[i])):
        cnt = 0
        ans = []
        for k in range(len(str_list[i][j])):
            if 'a' <= str_list[i][j][k] <= 'z' or 'A' <= str_list[i][j][k] <= 'Z':
                cnt += 1
        if isPowerOfTwo(cnt):
            ans.append('H')
        else:
            ans.append('C')
        print(*ans, end=' ')
    print()
