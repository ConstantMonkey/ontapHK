import math
a = float(input())
if 0<a<0.01:
    n = 0  
    s = 0  
    sohang = 1/math.factorial(1) 
    while sohang >= a:
        sohang = 1/math.factorial(2*n+1)  
        s += sohang  
        n += 1  
    print("S = {:.5f}".format(s))
