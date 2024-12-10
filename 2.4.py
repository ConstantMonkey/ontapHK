import math
a, b, c = map(float, input().split())
if a==0:
    if b==0:
        if c!=0:
            print("VN")
        else:
            print("VSN")
    else:
        x=-b/c
        print("x = {:.2f}".format(x))
else:
    delta = b**2 - 4*a*c
    if delta>0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("x1 = {:.2f}; ".format(x1) + "x2 = {:.2f}".format(x2))
    elif delta==0:
        x = -b/(2*a)
        print("x = {:.2f}".format(x))
    else:
        print("VN")