n = int(input())
flag = True
while n != 1:
    if int(n / 2) != n / 2:
        print('Неверно')
        flag = False
        break
    n = n / 2
if flag:
    print('Верно')
