def is_in1(x, y):
    return((abs(x)+abs(y)) <= 1)
print("YES" if is_in1(float(input()), float(input())) else "NO")