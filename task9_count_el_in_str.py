# Программа принивает на вход Строку и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n
# input: aaabcaadcdd
# output: aa_1a_2bca_3a_4dc_1d_1d_2

# stroka = input() # переменная и функция input для ввода
# stroka = stroka.split()# преобразовываем переменную в массив split(',') в скобках можно указать разделитель
stroka = input().split() # преобразовываем переменную в массив сразу.
# Создадим словарь в котором будет храниться наше значение
res = {}

for i in stroka:
    if i in res: # если буква i есть в нашем результате
        print(f'{i}_{res[i]}', end =' ') # вывадим через f строки '{i} наша буква _{res[i]} сколько раз она встречалась
        #, end=' ' все выводится в строку с разделителем пробел (если не указать end то все выводится на новой строке)
    else:
        print(i, end =' ') # если буквы нет в словаре, то выводим i через пробел
    res[i] = res.get(i,0) + 1 # обращаемся к словарю res[i] по ключу i
    # мы хотим получить значение которое находится по ключу i , если его нет то возвращается 0 и добавляется +1
    # если буква уже была, то проиходит переприсваивание 1+1=2 ...