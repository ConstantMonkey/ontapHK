n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
tong_chinh = 0  
tong_phu = 0  
for i in range(n):
    tong_chinh += A[i][i]
    tong_phu += A[i][n-i-1]
print(tong_chinh)
print(tong_phu)
