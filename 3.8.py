def thap_phan_sang_nhi_phan(n):
    if n == 0:
        return "0"  
    nhi_phan = ""  
    while n > 0:
        nhi_phan = str(n % 2) + nhi_phan 
        n = n // 2  
    return nhi_phan
n = int(input())
print(thap_phan_sang_nhi_phan(n))
