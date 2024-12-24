class NhanVien:
    def __init__(self,ten='',ma=0,heso=0,phucap=0):
        self.ten = ten
        self.ma = ma
        self.heso = heso
        self.phucap = phucap
    def nhap(self):
        self.ten,self.ma,self.heso,self.phucap = input().split()
        self.ma=int(self.ma)
        self.heso=float(self.heso)
        self.phucap=int(self.phucap)
    def luong_thang(self):
        return self.heso*2000000+self.phucap
    def xuat(self):
        return "{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma,self.ten,self.heso,self.phucap,self.luong_thang())
n = int(input())
ds=[]
for _ in range(n):
    nvien=NhanVien()
    nvien.nhap()
    ds.append(nvien)
luong_min = ds[0]
for nv in ds[1:]:
    if nv.luong_thang() < luong_min.luong_thang():
        luong_min = nv
print("Nhan vien co luong thap nhat")
print(luong_min.xuat())
