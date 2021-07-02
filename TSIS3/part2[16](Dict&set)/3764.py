
# import sys
#
# letS = str(sys.stdin.read()).split()
# myLets = {}
# for i in letS:
#     myLets[i] = myLets.get(i, 0) + 1
# myLets = [(fr, lt) for lt, fr in myLets.items()]  # menyaem mestami значение и ключ(коунтер)
#
#
# def makeSort(lws):
#     return -lws[0], lws[1] # не оч понял этот момент
#
#
# myLets.sort(key=makeSort)
# for i in range(len(myLets)):
#     print(myLets[i][1])


from collections import Counter
import sys

lets = str(sys.stdin.read()).split()

c = Counter(sorted(lets))
print(*sorted(c.keys(), key=c.get, reverse=True), sep='\n')
