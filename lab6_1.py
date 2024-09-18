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
    for i in cloths[n]:
        nord = []
        nord.extend(order)
        nord.append(i)
        shufle(n+1, nord)


c = int(input("Количество выводимых вариантов : "))
_c = 0
shufle(0)

res_it = list(itertools.islice(itertools.product(pl, bl, rl, gl, repeat=1), c))

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
for order in res_it:
    if i >= c: break
    print('Случай {:} : '.format(i + 1))
    i += 1
    for k in range(4):
        print(order[k], end=' ')
    print()
