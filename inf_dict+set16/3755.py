file = open('input.txt', 'r')
n = int(file.readline())
right = set(range(1, n + 1))
for line in file:
    if "YES" in line:
        right &= temp
    elif "NO" in line:
        right -= temp
    elif "HELP" in line:
        break
    else:
        temp = set(map(int, line.split()))
file.close()
print(' '.join(map(str, sorted(right))))

