# 16.По введенному числу (от 0 до 7) напечатать название цифры.
import random

number = random.randint(1, 8)
print('введенное число - ' + str(number))

match number:
    case 1:
        print('введенное число - ОДИН')
    case 2:
        print('введенное число - ДВА')
    case 3:
        print('введенное число - ТРИ')
    case 4:
        print('введенное число - ЧЕТЫРЕ')
    case 5:
        print('введенное число - ПЯТЬ')
    case 6:
        print('введенное число - ШЕСТЬ')
    case 7:
        print('введенное число - СЕМЬ')
    case _:
        print('введенное число - НЕОПРЕДЕЛЕНО')
