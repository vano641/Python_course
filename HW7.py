# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# ответ : 3 5

var1 = '5 5' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5' 

# Мое Рещение:

var2 = '10 20 30 40 50' # строка
var3 = '10 20 30 40 50'
a = var2.split() # преобразуем переменную var2(строку) в массив  данных "а" где элементы это 10 20 30 40 50
# , а не 1,0, ,2,0, ,3,0, ...(любой символ)
b = var3.split()
#print(a[1]) => 20

set_n = set() # создаем множество (уникальны значения)
for i in a:
    set_n.add(i) # заполняем множество из Массива "а"

set_m = set()
for i in b:
     set_m.add(i)

set_nm= set_n.intersection(set_m) # записываем в переменную результат Пересечения Двух Множеств
result = sorted(set_nm) # Сортируем множество по порядку
result = list(result)
for i in result: # Преобразовываем множество в список
    print(i, end=' ') # печатаем элементы через " "

#Решение Преподавателя:

mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')


