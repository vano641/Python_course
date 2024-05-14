# Ваша задача - написать программу, которая определит максимальное число ягод,
# которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Подсказка:
# Кусты располагаются по окружности. Это значит если собирающий модуль будет находиться на последнем кусте, 
# то он сможет собрать ягоды с последнего куста, предпоследнего и первого.

# Входные данные:
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. 
# Размер списка не превышает 1000 элементов.

# Выходные данные:
# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, 
# находясь перед некоторым кустом грядки.

# arr = [5, 8, 6, 4, 9, 2, 7, 3] => 19 (8+5+6)

# Мое Решение:
#arr = [5, 8, 6, 4, 9, 2, 7, 3]
#arr = [2, 4, 6, 8, 10]
arr = [2, 4, 10, 4, 2]
res = list() # Результирующий список, куда мы передаем Сумму: элемент[i] + элемент спереди[i] + элемент ссзади[i]
for i in range(len(arr)-1):
    res.append(arr[i] + arr[i+1] + arr[i-1]) # на каждом круге вычисляем сууму и записываем ее в Результ.список

res = sorted(res) # сортируем список от меньшего к большему(самый большой элемент будет последним)
print(res[-1]) # выводим последний элемент

# Решение Преподавателя:
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

# Вывод максимальной урожайности, которую может собрать собирающий модуль
print(max(arr_count))



