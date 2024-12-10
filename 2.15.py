import math
ep = float(input())
if 0<ep<1:
    x = float(input())
    sohang = 1  
    s = sohang  
    n = 1     
    while abs(sohang) >= ep:
        sohang = (x**n)/math.factorial(n)  
        s += sohang  
        n += 1   
    print("{:.6f}".format(s))
