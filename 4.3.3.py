m, n_a = map(int, input().split())  
n_b, p = map(int, input().split())
if n_a != n_b:
    print("So cot A phai bang so hang B")
else:
    A = [list(map(int, input().split())) for _ in range(m)]
    B = [list(map(int, input().split())) for _ in range(n_a)]
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n_a):
                C[i][j] += A[i][k] * B[k][j]
    for hang in C:
        print(*hang)
    