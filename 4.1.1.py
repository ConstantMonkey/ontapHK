import bisect
n, k = map(int, input().split())
a = list(map(int, input().split()))
so = list(map(int, input().split()))
for x in so:
    idx = bisect.bisect_left(a, x)
    if idx < n and a[idx] == x:
        print("YES")
    else:
        print("NO")