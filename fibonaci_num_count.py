# Дано натуральное число A > 1. Определить каким по счету числом Фибоначчи оно является f(n)=A .
# Если А не является числом Фибоначчи, выведите число -1
# A = 5 => f(n) = 6 т.к числа Фибоначчи 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987...

A = int(input('Введите А: '))
fibonacci1 = 0
fibonacci2 = 1
res = 0 # сумма двух чисел фибоначчи
i = 2 # т.к первые 2 числа мы уже записали 0 и 1
if A > 1:
    while res < A: # пока сумма двух чисел меньше введенного числа А
        res = fibonacci1 + fibonacci2
        fibonacci1 = fibonacci2
        fibonacci2 = res
        i += 1
        if res > A: #  если сумма больше введенного числа, значит оно не является числом Фибоначчи
            i = -1
print(i) # ввыводим порядковый номер введенного числа в последовательности Фибоначчи