# . Создайте итерируемый объект, возвращающий генератор
# тридцати пяти чисел трибоначчи и выведите эти числа.

def Gen3(n):
    a, b, c = 0, 0, 1
    for __ in range(n):
        yield a
        a, b, c = b, c, a + b + c


print(list(Gen3(35)))