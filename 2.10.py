import math
n = int(input())
x = int(input())
s = x
for i in range(1, n+1):
    s = math.sqrt(x + s) 
s = s + 1  
print(s)