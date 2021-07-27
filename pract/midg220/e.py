for i in range(1):
    s = input().split()
    print(max(s, key=len), len(max(s, key=len)), sep='\n')
