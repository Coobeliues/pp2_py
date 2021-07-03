# print(' '.join(sorted(set(input().split()).intersection(set(input().split())))))
print(*sorted(set(input().split()) & set(input().split()), key=int))
