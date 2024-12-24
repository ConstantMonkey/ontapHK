chuoi_so = input()
ds = chuoi_so.split(",")
so_le = [int(so.strip()) for so in ds if int(so.strip()) % 2 != 0]
print(", ".join(map(str, so_le)))
