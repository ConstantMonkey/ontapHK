s = input()
dem_hoa = 0
dem_thuong = 0
dem_so = 0
for char in s:
    if char.isupper():  
        dem_hoa += 1
    elif char.islower(): 
        dem_thuong += 1
    elif char.isdigit():
        dem_so += 1
print("Chu viet hoa: {}".format(dem_hoa))
print("Chu viet thuong: {}".format(dem_thuong))
print("So: {}".format(dem_so))
