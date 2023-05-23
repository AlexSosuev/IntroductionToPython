# Задача №47. 
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
transformation = lambda x:x**x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transormed_values = list(map(transformation, values))
print(transormed_values)
# Задача №49. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, #орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая #среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не #учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были #запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса #орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее #эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При #решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: #сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. #Гарантируется, что самая далекая планета ровно одна

from functools import reduce

def find_farthest_orbit(list_of_orbits):
    list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))    
    find_farthest_orbit = reduce(lambda a, b: a if a[0] * a[1] > b[0] * b[1] else b, list_of_orbits)
    print(*find_farthest_orbit)    

def find_farthest_orbit2(list_of_orbits):
    return max(list_of_orbits, key = lambda x: (x[0]!=x[1])*x[0]*x[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
find_farthest_orbit(orbits)
print(*find_farthest_orbit2(orbits))

# Просто задача
l=[1,3,4,5,2]
print(sorted(l, key=lambda x: x % 2 == 0))

# Задача №51. Решение в группах Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если  #это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора #объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект #и вычисляет его характеристику.
def func(x):
    return x % 2 == 0

def same_by(characteristic, object):
    return len(list(filter(characteristic, object))) == len(object)   

values = [0, 2, 10, 6]
characteristic = lambda x: x % 2 == 0
if same_by(characteristic, values):
    print('same')
else:
    print('different')

# Замыкание
def test(x):
    def f(n):
        return n % x == 0
    return f

f = test(2)
print(f(8))
# -------------------------------------------
same_list1 = [1,2,3,4]
same_list2 = ['a','b','c','d','e']

print(list(zip(same_list1,same_list2)))
print(tuple(zip(same_list1,same_list2)))
my_dict = dict(zip(same_list2,same_list1))
# -------------------------------------------
def func(a, b, c, d):
    return a + b + c + d

print(func(**my_dict))
# -------------------------------------------
def func02(**kwargs):
    print(kwargs)

func02(a=4, b=7, c=2)
# -------------------------------------------
def func03(*args):
    return sum(args)

print(func03(1,2,3,4,5,6))
# -------------------------------------------
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
print(d)