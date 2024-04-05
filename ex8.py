n = int(input())
k = 1
while (n / 2) > 1:
    if int(n / 2) == n / 2:
        n = int(n/2)
    else:
        n = int(n/2) + 1
    k += 1
print(k)
