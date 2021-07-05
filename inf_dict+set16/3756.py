file = open('input.txt', 'r')
n = int(file.readline())
right = set(range(1, n + 1))
for line in file:
    if "HELP" in line:
        break
    else:
        temp = set(map(int, line.split()))
        if len(right & temp) > len(right) / 2:
            print('YES')
            right &= temp
        elif len(right & temp) <= len(right) / 2:
            print('NO')
            right -= temp
file.close()
print(' '.join(map(str, sorted(right))))

