N, Q = map(int, input().split())
S = input()
dem = [[0] * (N+1) for _ in range(26)] 
for i in range(1, N+1):
    chi_so = ord(S[i-1]) - ord('a')  
    for j in range(26):
        dem[j][i] = dem[j][i-1]
    dem[chi_so][i] += 1
kq = []
for _ in range(Q):
    L, R, C = input().split()
    L, R = int(L), int(R)
    chi_so = ord(C) - ord('a') 
    kq.append(dem[chi_so][R] - dem[chi_so][L-1])
print("\n".join(map(str, kq)))
