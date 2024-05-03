# Найти в массиве list_1 самы близкий по значению элемент к Заданному числу k.
# Считать, что такой элемент может быть всего 1.
# Если значение k совпадает с этим элементом - вывести его.
# list_1 = [1,2,3,4,5]; k = 6; => ответ 5

list_1 = [1, 4, 3, 7, 8, 9, 2]

# Мое Решение:
k = int(input('введите k: '))
result = 0
for i in range(len(list_1)):
    if k == list_1[i]:
        result = list_1[i]
        break
    if k - 1 == list_1[i] or k + 1 == list_1[i]:
        result = list_1[i]
print(result)

# Решение преподавателя
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print('решение преподавателя',number)
