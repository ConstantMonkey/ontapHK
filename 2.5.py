a1, b1, c1 = map(float, input().split())
a2, b2, c2 = map(float, input().split())
D = a1*b2-a2*b1
Dx = c1*b2-c2*b1
Dy = a1*c2-a2*c1
if D!=0:
    x = Dx/D
    y = Dy/D
    print("x = {:.2f}; ".format(x) + "y = {:.2f}".format(y))
elif Dx==0 and Dy==0:
    print("VSN")
else:
    print("VN")