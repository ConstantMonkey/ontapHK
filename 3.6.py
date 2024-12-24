def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
n = int(input())
tong = 0
for i in range(1, n + 1):
    fibonacci_n = fibonacci(i)
    sohang = fibonacci(1) / fibonacci_n
    print("Fibonacci(1) / Fibonacci({}) = {:.5f}".format(i, sohang))
    tong += sohang
print("Tong: {:.5f}".format(tong))
