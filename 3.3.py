def hoanhao(n):
    if n<=1:
        return False
    tong=0
    for i in range(1, n//2+1):
        if n%i==0:
            tong=tong+i
    return tong==n
a, b = map(int, input().split())
for i in range(a + 1, b):
    if hoanhao(i):
        print(i, end=" ")
