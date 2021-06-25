m = 1
dec = 1
inc = 1
n1 = int(input())
while n1:    
    m = max(inc, dec, m)
    n2 = int(input())
    if not n2: break
    if n1 > n2: dec, inc = dec + 1, 1               
    elif n1 < n2: inc, dec = inc + 1, 1        
    else: inc = dec = 1
    n1 = n2
print(format(m))
