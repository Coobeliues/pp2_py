for i in range(int(input())):
    cnt = 0
    s = input().split()
    if len(s) % 2 == 0 and s[0].istitle() and s[-1].count('3') == 2:
        for j in range(len(s)):
            if (j % 2 == 0 and len(s[j]) % 2 != 0) or (j % 2 != 0 and len(s[j]) % 2 == 0):
                cnt += 1
    print('Wow! That is perfect' if cnt == len(s) else 'Seriously?')
