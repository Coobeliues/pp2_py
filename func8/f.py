from math import sqrt
def is_in_area(x, y):
    intri = bool(((x+y) <= 0) and (abs(x) <= 3.5) and (0 > y >= -3.5))
    inro_f_o = bool(((sqrt((abs((-1)-x) ** 2) + (abs(1-y) ** 2)) + 0.05) <= 2))
    inro = bool((sqrt((abs((-1)-x) ** 2) + (abs(1-y) ** 2)) <= 2))
    intri_s = bool((0.5 <= y <= 3) and (1 >= x >= -3) and (1 < (x+y) <= 3))
    return((intri and not inro_f_o) or (inro and intri_s))
print("YES" if is_in_area(float(input()), float(input())) else "NO")
#не решено
