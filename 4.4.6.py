class SinhVien:
    def __init__(self,ten='',ma=0,diem_toan=0,diem_triet=0,diem_LTC=0):
        self.ten = ten
        self.ma = ma
        self.diem_toan = diem_toan
        self.diem_triet = diem_triet
        self.diem_LTC = diem_LTC
    def nhap(self):
        self.ten,self.ma,self.diem_toan,self.diem_triet,self.diem_LTC = input().split()
        self.ma = int(self.ma)
        self.diem_toan = float(self.diem_toan)
        self.diem_triet = float(self.diem_triet)
        self.diem_LTC = float(self.diem_LTC)
    def diem_TB(self):
        return round((self.diem_toan+self.diem_triet+self.diem_LTC)/3, 2)
    def xuat(self):
        return "{} {} {:.2f} {:.2f} {:.2f} {:.2f}".format(self.ma,self.ten,self.diem_toan,self.diem_triet,self.diem_LTC,self.diem_TB())
    def sv_hoclai(ds):
        return [sv for sv in ds if (sv.diem_toan<4 and sv.diem_triet<4) 
                or (sv.diem_toan<4 and sv.diem_LTC<4) 
                or (sv.diem_triet<4 and sv.diem_LTC<4) 
                or (sv.diem_toan<4 and sv.diem_triet<4 and sv.diem_LTC<4)]
n = int(input())
ds_sv = []
for i in range(n):
    sv = SinhVien()
    sv.nhap()
    ds_sv.append(sv)
print("Danh sach sien hoc lai")
ds_hoclai = SinhVien.sv_hoclai(ds_sv)
for i in ds_hoclai:
    print(i.xuat())
print("Danh sach nay co {} sinh vien phai hoc lai".format(len(ds_hoclai)))