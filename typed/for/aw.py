n=int(input())
import math
from math import sqrt
for x in range(1, int(math.ceil(sqrt(n+1)))):
    print(x*x)