# 15 Удалить элементы, индексы которых кратны 3.
import random

number = int(input("Введите размер списка:\n"))
array = [random.randint(0, 99) for _ in range(number)]
arrayNew = []
print('начальный список: ' + str(array))
for i in range(len(array)):
    if i % 3 != 0 or i == 0:
        arrayNew.append(array[i])
print('конечный список: ' + str(arrayNew))
