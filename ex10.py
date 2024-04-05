n = 1
ns = 0
k = 0
while n != 0:
    n = float(input())
    if (ns > n) and (n != 0):
        k += 1
    ns = n
print(k)
