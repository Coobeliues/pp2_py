# students = [{input() for j in range(int(input()))} for i in range(int(input()))]
# known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
# print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
# print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
#


l = []
for i in range(int(input())):
    st = set()
    for j in range(int(input())):
        st.add(input())
    l.append(st)
everybod = list(set.intersection(*l))
nobod = list(set.union(*l))
print(len(everybod), *sorted(everybod), sep='\n')
print(len(nobod), *sorted(nobod, reverse=True), sep='\n')
