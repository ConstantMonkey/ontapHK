def ma_hoa_xau(s):
    ma_hoa = ""  
    dem = 1  
    for i in range(1, len(s)):
        if s[i] == s[i-1]:  
            dem += 1
        else:  
            ma_hoa += s[i-1] + str(dem)
            dem = 1
    if s:
        ma_hoa += s[-1] + str(dem)
    return ma_hoa
t = int(input())
kq = []
for _ in range(t):
    s = input().strip()
    kq.append(ma_hoa_xau(s))
print("\n".join(kq))
