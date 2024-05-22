# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен 
# input:  print_operation_table(lambda x, y: x * y, 3, 3)
# output:
# 1 2 3
# 2 4 6 
# 3 6 9

# Мое Решение:
def print_operation_table(operation, num_rows = 9 , num_columns = 9 ): # Метод в который передаем Функцию(x*y)
# и значения X,Y = 9 по умолчанию, если их НЕ задают в print_operation_table(lambda x, y: x * y), если они задаются, то
# num_rows b num_columns получают значения X и У из print_operation_table(lambda x, y: x - y, 5, 5)
    res = list()
    if num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1): # перебераем значения от 1(исключаем 0) до X (num_rows)
            for j in range(1, num_columns + 1): # перебераем значения от 1(исключаем 0) до Y (num_columns)
                res.append(operation(i,j)) # добавляем в результирующий список Результат работы Ф-ции operation(lambda)
            print(*res) # печатаем список в строку без скобок и запятых через пробел
            res.clear() # Очищаем список перед Следующей итерацией
         

print_operation_table(lambda x, y: x * y)
# print_operation_table(lambda x, y: x * y)
# print_operation_table(lambda x, y: x * y, 9, 9)
# print_operation_table(lambda x, y: x - y, 5, 5)

# Решение Преподавателя:
def print_operation_table(operation, num_rows=9, num_columns=9):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n') # '\n' обозначает окончание строки и перенос на новую строку
#(каждый новый цикс i начинается с новой строки)
        print(''.join([str(i) for i in result[:len(result) - 1]])) 
# .join объединяет элементы списка в строку с указанным в '' разделителем

print_operation_table(lambda x, y: x * y, 3, 3)


     
        
