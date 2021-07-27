def anagram(str1, str2):
    str1_list = list(str1)

    str2_list = list(str2)

    for i in range(len(str1_list)):
        return str1_list[i] == str2_list[i]


a = [str(i) for i in input().split()]
t = set(a)

tt = set()

for i in t:
    if anagram(i, reversed(i)):
        tt.add(i)

print(*sorted(t-tt), sep='\n')
