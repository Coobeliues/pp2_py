n = input()
miss = [str(i) for i in input().split()]
m = input()
noti = [str(i) for i in input().split()]

for i in range(len(miss)):
    cnt = 1
    for j in range(len(noti)):
        if miss[i] == noti[j]:
            cnt += 1
    if cnt % 2 != 0:
        print(miss[i])
for i in range(len(miss)):
    cnt = 1
    for j in range(len(noti)):
        if noti[i] == miss[j]:
            cnt += 1
    if cnt % 2 != 0:
        print(noti[i])