# Вычислить факториал заданного числа n используя цикл While
# n = 5  => N! = 1 * 2 * 3 * 4 * 5 = 120

n = int(input('Введите n: '))
N = 1 
result = 1
while N <= n:
    result = N * result
    N = N + 1
print('Факториал числа', n, '=', result)
