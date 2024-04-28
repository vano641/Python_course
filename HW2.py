# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.
# s = 12 (3 + 9)
# p = 27 (3 * 9) => 3 9

# Мое Решение

s = 17
p = 72
res = 0
for i in range(s):
    for j in range(s):
        if i * j == p and i <= j and i + j == s:
            print(i,j)

# Решение в автотестах 

#solutions = []
#for i in range(1, 1001):
#    for j in range(1, 1001):
#        if s == i + j and p == i * j:
#            solutions.append((min(i, j), max(i, j)))
#solutions = list(set(solutions))

#for solution in solutions:
#    print(solution[0], solution[1])
