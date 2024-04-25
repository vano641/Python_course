#a, b, c = 3, 2, 4 -> yes
#a, b, c = 3, 2, 1 -> no

a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

if c <= a * b and (c % a == 0 or c % b == 0) :
    print('yes')
else:
    print('no')



