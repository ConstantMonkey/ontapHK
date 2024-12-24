import re
s = input()
tap_so = re.findall(r'\d+', s)
tap_so_max = max(map(int, tap_so)) if tap_so else 0
print(tap_so_max)