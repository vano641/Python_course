# Сколько раз встречается число k в массиве list_1
# Найти количество и вывести его
# list_1 = [1,2,3,4,5]; k = 3; => ответ : 1

list_1 = [1, 2, 3, 4, 5, 3, 3, 5, 7,2,2,2,22,2,22,222,22,2,22,22]
k = int(input('введите к: '))
count = 0
for i in range(len(list_1)):
    if k == list_1[i]:
        count += 1
if count == 0:
    print('число к не найдено')
print('ответ',count)
