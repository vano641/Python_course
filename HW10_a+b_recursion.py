# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы
# sum(2, 2) => 4

# Мое Решение:
a = 16
b = 6

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
print(sum(a,b))

# Решение Преподавателя
def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)
a = 16
b = 6
print(sum(a,b))