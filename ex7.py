n = int(input())
flag = True
k = 0
while n != 1:
    if int(n / 2) != n / 2:
        flag = False
        break
    n = n / 2
    k += 1
if flag and k > 0:
    print('Верно')
else:
    print('Неверно')