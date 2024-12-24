m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
tong_mt = sum(sum(row) for row in A)
so_ptu = m * n
tbc = tong_mt / so_ptu
print("{:.2f}".format(tbc))
for i in range(m):
    for j in range(n):
        if A[i][j] > tbc:
            print(A[i][j], i+1, j+1)  
