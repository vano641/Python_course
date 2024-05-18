# Напишите функцию same_by(characteristic, objects), которая проверяет
# все ли обьекты имеют Одинаковое значение Некоторой характеристики (например четность),
# и возвращают True если это так. Если значение хар-ки для разных обьектов отличается - False
# Для пустого набора обьектов - True
# Аргумент characteristic - это функция, которая принимает Обьект и вычисляет его характеристику
# input:
# values = [0, 2, 10, 6]
# if same_by(lambada x: x % 2, values): # проверка на четность
#     print('same')
# else:
#     print('different')

# output: => same

def same_by (characteristic, object):
    result = True # переменная в которую записываем результат True или False
    list1 = [characteristic(x) for x in object] # список в котором каждый элемент это результат работы
# нашей Функции chracteristic (x % 2) к нашему списку object(values)
# chracteristic применяем к каждому элементу x в object 
    for i in range(len(list1) - 1): # проверим одинаковы ли свойства у объектов (-1 т.к проверка условия i+1)
        if list1[i] != list1[i + 1]: # если обьекты с разными характеристиками (i[0] четное, а i[1] не четное)
            result = False # тогда не у всех элементов одинаковые характеристики
    return result

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values): # проверка на четность
    print('same')
else:
    print('different')