s = input()
dem = {}
for chu in s:
    if chu in dem:  
        dem[chu] += 1
    else:
        dem[chu] = 1
for chu, count in dem.items():
    print("'{}': {}".format(chu, count))
