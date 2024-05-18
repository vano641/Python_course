# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется
# множество раз и вы не хотите ничего сломать)

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] или любой другой список.
# transformed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть.

# Напишите такое Лямбда-выражение transformation, чтобы transformed_values получился копией values
# Пример:
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#       print('ok')
# else:
#       print('false')
# Решение:

transformation = lambda x: x # чтобы список остался такимже мы будем просто передавать х
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
transformed_values = list(map(transformation, values)) # map применяет функцию transformation к каждому элементу values
if values == transformed_values:
    print('ok')
else:
    print('false')