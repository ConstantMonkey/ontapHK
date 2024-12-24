n = int(input())  
A = [list(map(int, input().split())) for _ in range(n)]  
dx = True  
for i in range(n):
    for j in range(i, n): 
        if A[i][j] != A[j][i]:
            dx = False
            break
    if not dx:
        break
if dx:
    print("YES")
else:
    print("NO")
