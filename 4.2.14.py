import re
def sap_xep_so_trong_xau(s):
    so = [int(num) for num in re.findall(r'\d+', s)]
    so.sort()
    so_da_xep = iter(so)
    def replace(match):
        return str(next(so_da_xep))
    kq = re.sub(r'\d+', replace, s)
    return kq
s = input()
print(sap_xep_so_trong_xau(s))
