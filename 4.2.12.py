import re
s = input()
tap_so = re.findall(r'\d+', s)
tong = sum(map(int, tap_so)) if tap_so else 0
print(tong)