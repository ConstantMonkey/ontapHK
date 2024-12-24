def chuan_hoa(line):
    ds_tu = line.strip().split()
    for i in range(len(ds_tu)):
            ds_tu[i] = ds_tu[i].lower().capitalize()  
    return ' '.join(ds_tu)
cau = input()
print(chuan_hoa(cau))