import math
n = int(input())
s = 0
for i in range(1, 2*n+1, 2):
    s = s + 1/(math.factorial(i) )
print(s)

N = 1
S = 0
while S<=1000:
    S = S+N
    N = N+1
print("Số nguyên dương n nhỏ nhất sao cho tổng lớn hơn 1000 là:", N-1)