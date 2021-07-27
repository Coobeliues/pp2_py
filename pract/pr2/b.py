def anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()

    str2_list = list(str2)
    str2_list.sort()

    return str1_list == str2_list


f = open('i.txt', 'r')
file = f.read().split('\n')

s = file[0]
t = set(file[1:])

tt = set()

for i in t:
    if anagram(i, s):
        tt.add(i)
print(*sorted(t - tt))
