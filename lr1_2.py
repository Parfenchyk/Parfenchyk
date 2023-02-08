# 5. Дана непустая последовательность ненулевых целых чисел, за которой следует 0.
# Определить, сколько раз в этой последовательности меняется знак.
import random

number = int(input("Введите размер списка:\n"))
array = [random.randint(-99, 99) for _ in range(number)]
arrayNew = []
for i in range(len(array)):
    if array[i] != 0:
        arrayNew.append(array[i])
arrayNew.append(0)
print('начальная последовательность: ' + str(arrayNew))

count = 0
for i in range(len(arrayNew) - 2):
    if (arrayNew[i] > 0 and arrayNew[i + 1] > 0) or (arrayNew[i] < 0 and arrayNew[i + 1] < 0):
        continue
    else:
        count += 1
    i += 1
print('Количество изменений знака в последовательности: ' + str(count))
