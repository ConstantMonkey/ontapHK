m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(m)]
C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
D = [[A[i][j] - B[i][j] for j in range(n)] for i in range(m)]
for hang in C:
    print(' '.join(map(str, hang)))
for hang in D:
    print(' '.join(map(str, hang)))
