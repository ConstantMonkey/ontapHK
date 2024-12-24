n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
tg_tren = True
tg_duoi = True
for i in range(n):
    for j in range(n):
        if i>j and A[i][j]!=0:
            tg_tren = False
        if i<j and A[i][j]!=0:   
            tg_duoi = False
if tg_tren:
    print("UPPER TRIANGLE")
elif tg_duoi:
    print("LOWER TRIANGLE")
else:
    print("NONE")
