# Дано натуральное число N и последовательность из N элементов.
# Вывести эту последовательность в обратном порядке.
# Примечание:
# В программе запрящается объявлять массивы и использовать циклы (даже для ввода и вывода)
# input 2 => 3 4
# output => 4 3

# Будем использовать Рекурсию

def f(n):
    if n == 0: # когда мы из n - 1 , то при n==0 мы останавливаемся и выводим пустую строку
        return '' # это База (выход из рекурсии)
    k = int(input()) # вводим последовательность (число k элементы последовательности)
    return f(n - 1) + f'{k}' # вызываем саму рекурсию f(n-1), а введенный элемент записывается а +f'{k}'

n = int(input()) # кол-во элементов последовательности
print(f(n))

# Пример: 
# 1) вводим 2 (кол-во элементов) => n=2
# 2) n==0 не соблюдается
# 3) вводим k = 3
# 4) f(n - 1) + f'{k}'
# 5)  2-1=1       +'3' (Тройка записалась в конец, далее n-1 и рекурсия вызывается повторно)
# 6) вводим k = 4
# 7)  1-1=0    ''    +'4'   +'3'
# 8) рекурсия завершается и выводится строка 43