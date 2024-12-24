def tong_so(n):
    n = abs(n)  
    tong = 0
    while n > 0:
        tong += n % 10 
        n //= 10  
    return tong
try:
    so = int(input())
    kq = tong_so(so)
    print(kq)
except ValueError:
    print()
