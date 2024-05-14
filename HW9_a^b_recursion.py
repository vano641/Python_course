# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

# Мое Решение:
a = 3
b = 5
def f(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return (a * f(a, b - 1))
print(f(a,b))

# Решение Преподователя
def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a # пока b не дойдет до 0 мы a*a в каждой итерации рекурсии

a = 3
b = 5
print(f(a,b))