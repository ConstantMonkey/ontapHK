class Sach:
    def __init__(self,ten='',trang=0,gia=0):
        self.ten = ten
        self.trang = trang
        self.gia = gia
    def nhap(self):
        self.ten = input()
        self.trang = int(input())
        self.gia = float(input())
    def gia_tb(self):
        return round(self.gia/self.trang, 2) if self.trang>0 else 0
    def xuat(self):
        return "{}, {}, {}, {}".format(self.ten,self.trang,self.gia,self.gia_tb())
n = int(input())
books = []
for i in range(n):
    print("Quyen sach thu",i+1)
    book = Sach()
    book.nhap()
    books.append(book)
books.sort(key=lambda x: (x.gia_tb(), x.ten))
with open("sach2.txt", "w", encoding="utf-8") as file:
    for b in books:
        file.write(b.xuat()+"\n")
# try:
#     with open("sach2.txt", "r", encoding="utf-8") as file:
#         print("File sach2.txt sap xep tang dan theo gia tb/ten:")
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print("File sach2.txt khong ton tai!")