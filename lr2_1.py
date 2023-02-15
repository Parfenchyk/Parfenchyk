# Вариант 5
# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.
#

array = [8, 19, 0, -9, 1, -3, 5, 7, 0, 13]
array.sort()
a1 = 0
for i in range(len(array)):
    if array[i] % 2 == 0 and array[i] != 0:
        a1 = array[i]
        print('наименьший чётный элемент: ' + str(a1))
        break
if a1 % 2 != 0 or a1 == 0:
    print('первый элемент: ' + str(array[0]))



arrayNew = []
for i in range(len(array)):
    if array[i] == 0:
        arrayNew.append(array[i])
for i in range(len(array)):
    if array[i] != 0:
        arrayNew.append(array[i])
for i in range(len(array)):
    print('элементы списка, начиная с нуля: ' + str(arrayNew[i]))


