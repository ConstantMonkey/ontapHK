class Sach:
    def __init__(self,name='',page=0,cost=0):
        self.name=name
        self.page=page
        self.cost=cost
    def nhap(self):
        self.name=input()
        self.page=int(input())
        self.cost=float(input())
    def average(self):
        return round(self.cost/self.page,2) if self.page>0 else 0
    def xuat(self):
        return "{}, {}, {}, {}".format(self.name,self.page,self.cost,self.average())
n=int(input())
books=[]
for i in range(n):
    print("Quyen sach thu",i+1)
    book=Sach()
    book.nhap()
    books.append(book)
books.sort(key=lambda s:s.average(), reverse=True)
with open("sach1.txt", "w", encoding="utf-8") as file:
    for b in books:
        file.write(b.xuat()+"\n")
# try:
#     with open("sach1.txt", "r", encoding="utf-8") as file:
#         print("File sach1.txt sap xep giam dan:")
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print("File sach1.txt khong ton tai!")