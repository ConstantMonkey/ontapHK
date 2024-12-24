m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(m)]
tong = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
for hang in tong:
    print(*hang)