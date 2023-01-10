#ПРОТОТИПЫ
#1 Делимость
#flag
for a  in range(1, 1000):
    flag = 0
    for x in range(1, 1000):
        if (((x % a != 0) and (x % 21 == 0)) <= (x % 14 == 0)) == 0:
            flag = 1
            break
        if flag == 0:
            print(a)


    