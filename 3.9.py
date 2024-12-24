def thap_phan_sang_thap_luc_phan(n):
    if n == 0:
        return "0"  
    ki_tu = "0123456789ABCDEF"  
    thap_luc_phan = ""  
    while n > 0:
        thap_luc_phan = ki_tu[n % 16] + thap_luc_phan  
        n = n // 16 
    return thap_luc_phan
n = int(input())
print(thap_phan_sang_thap_luc_phan(n))
