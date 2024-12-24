def chuan_hoa(line):
    ds_tu = line.strip().split()
    if ds_tu:
        ds_tu[0] = ds_tu[0].capitalize()  
    return ' '.join(ds_tu)
cau = input()
print(chuan_hoa(cau))
