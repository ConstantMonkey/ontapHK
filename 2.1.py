a, b = map(int, input().split())
if a==0:
    if b!=0:
        print("VN")
    else:
        print("VSN")
else:
    x=-b/a
    print("x = {:.2f}".format(x))