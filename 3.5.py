def ucln(a, b):
    while b!=0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a*b)/ucln(a, b)
a, b = map(int, input().split())
print(bcnn(a, b))
