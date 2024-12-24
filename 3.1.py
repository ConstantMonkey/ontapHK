def giaithua(n):
    if n==0 or n==1:
        return 1
    else:
        kq = 1
        for i in range(2, n+1):
            kq = kq*i
        return kq
n = int(input())
if n>0:
    print(giaithua(n))
