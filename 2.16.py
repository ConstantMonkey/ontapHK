import math
a, b, c = map(float, input().split())
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        p = (a+b+c)/2
        S = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Chu vi: {:.2f}".format(2*p))
        print("Dien tich: {:.2f}".format(S))
    else:
        print("Khong la tam giac.")