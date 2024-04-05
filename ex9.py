a = list(map(int, input().split()))
n = a[0]
k = a[1]
r = a[2]
day = 1
while n < r:
    n = n + n * (k / 100)
    day += 1
print(day)
