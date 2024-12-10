import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
S = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
if S==0:
    print("Khong la tam giac.")
else:
    a = math.sqrt((x2-x3)**2+(y2-y3)**2)  
    b = math.sqrt((x1-x3)**2+(y1-y3)**2)  
    c = math.sqrt((x1-x2)**2+(y1-y2)**2) 
    P = a+b+c   
    print("Chu vi: {:.2f}".format(P))
    print("Dien tich: {:.2f}".format(S))