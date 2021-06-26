def isPointInSquare(x: float, y: float, v: float) -> bool:
    return (v  >= abs(x) ) and (v  >= abs(y))

x, y = float(input()), float(input())

print("YES" if isPointInSquare(x, y, 1) else "NO")