'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 27. У юноши P пиджаков, B брюк, R рубашек, G галстуков.
Составьте все возможные костюмы из этих предметов.
Усложнение: за чётным элементом одежды след нечетный, за нечетным - чётный
'''
import itertools
import math

orders = []
_c = 0

p = int(input('Количество пиджаков = '))
b = int(input('Количество брюк = '))
r = int(input('Количество рубашек = '))
g = int(input('Количество галстуков = '))

pl = ['Пиджак ' + str(i+1) for i in range(p)]
bl = ['Брюки ' + str(i+1) for i in range(b)]
rl = ['Рубашка ' + str(i+1) for i in range(r)]
gl = ['Галстук ' + str(i+1) for i in range(g)]

cloths = [pl, bl, rl, gl]

def shufle(n, order=[]):
    if n == 4:
        orders.append(order)
        return
    for i in range(len(cloths[n])):
        if n > 0:
            if (int(order[-1][-1]) % 2) == ((i + 1) % 2): continue
        nord = []
        nord.extend(order)
        nord.append(cloths[n][i])
        shufle(n+1, nord)


c = int(input("Количество выводимых вариантов : "))
_c = 0
shufle(0)

pl1 = ['Пиджак ' + str(i+1) for i in range(0, p, 2)]
bl1 = ['Брюки ' + str(i+1) for i in range(0, b, 2)]
rl1 = ['Рубашка ' + str(i+1) for i in range(0, r, 2)]
gl1 = ['Галстук ' + str(i+1) for i in range(0, g, 2)]

pl2 = ['Пиджак ' + str(i+1) for i in range(1, p, 2)]
bl2 = ['Брюки ' + str(i+1) for i in range(1, b, 2)]
rl2 = ['Рубашка ' + str(i+1) for i in range(1, r, 2)]
gl2 = ['Галстук ' + str(i+1) for i in range(1, g, 2)]

res_it_1 = list(itertools.islice(itertools.product(pl1, bl2, rl1, gl2, repeat=1), c))
res_it_2 = list(itertools.islice(itertools.product(pl2, bl1, rl2, gl1, repeat=1), c))

print('Результат работы алгоритма : ')
i = 0
for order in orders:
    if i >= c: break
    print('Случай {:} : '.format(i + 1))
    i += 1
    for k in range(4):
        print(order[k], end=' ')
    print()

print('\nРезультат работы itertools : ')
i = 0
for order in res_it_1:
    if i >= c: break
    print('Случай {:} : '.format(i + 1))
    i += 1
    for k in range(4):
        print(order[k], end=' ')
    print()

for order in res_it_2:
    if i >= c: break
    print('Случай {:} : '.format(i + 1))
    i += 1
    for k in range(4):
        print(order[k], end=' ')
    print()
