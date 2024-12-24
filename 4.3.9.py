m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
tim = False
for i in range(m):
    tong_hang = sum(A[i])
    if tong_hang%7==0:
        print(i+1) 
        tim = True
if not tim:
    print("NO")
