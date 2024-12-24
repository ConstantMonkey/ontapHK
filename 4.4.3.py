class Sach:
    def __init__(self,name='',page=0,cost=0):
        self.name = name
        self.page = page
        self.cost = cost
    def __str__(self):
        return "{} {} {}".format(self.name, self.page, self.cost)
def doc_file(input_file):
    ds_sach = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            name, page, cost = line.strip().split()
            ds_sach.append(Sach(name, int(page), int(cost)))
    return ds_sach
def ghi_file(output_file, books):
    with open(output_file, "w", encoding="utf-8") as file:
        for b in books:
            file.write(str(b)+"\n")
def loc_sach(dsach):
    return [book for book in dsach if book.cost>100000 and book.page<200]
ds_sach = doc_file("D:\Python\ÔnHK_Chương4\sach.txt")
books_loc = loc_sach(ds_sach)
ghi_file("ketqua.txt", books_loc)
# with open("ketqua.txt", "r", encoding="utf-8") as file:
#     print("Danh sach tu file ketqua.txt:")
#     for line in file:
#         print(line.strip())