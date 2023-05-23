

# Задача 39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# Функция заполнения списка с клавиатуры
# def create_spisok(n):
#     return [int(input()) for _ in range(n)]


# N = int(input("Введите длину первого списка: "))
# some_list1 = create_spisok(N)
# M = int(input("Введите длину второго списка: "))
# some_list2 = create_spisok(M)

# for i in range(len(some_list1)):
#     if some_list1[i] not in some_list2:
#         print(some_list1[i], end=' ')

# Задача 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.


def create_spisok(n):
    return [int(input()) for _ in range(n)]

N = int(input("Введите длину списка: "))
some_list = create_spisok(N)

count = 0
for i in range(1, N-1):
    if some_list[i-1] < some_list[i] > some_list[i+1]:
        count += 1

print(f'Количество элементов, удовлетворяющих условию, равно - {count}')

# Задача 1. Определить простое число или нет рекурсией
# def prosto(n, t=2):
#     if n ==2:
#         return True
#     if n % t ==0:
#         return False
#     elif t*t > n:
#         return True
#     return prosto(n, t+1)


# def prost(n, div=None):
#     div = n // 2 + 1 if div is None else div
#     while div >= 2:
#         return False if n % div == 0 else prost(n, div - 1)
#     else:
#         return True

# n = int(input("Введите число: "))
# print("Число является простым") if prost(n) else print("Число не является простым")

# Задача 2. Полиндром?

# def palidrom(stroka, i = 0):
#     if stroka[i] != stroka[len(stroka)-i-1]:
#         return False
#     elif i > len(stroka) / 2: return True
#     else:
#         return palidrom(stroka, i + 1)

# def polindrom(txt):
#     if len(txt) < 2:
#         return True
#     if txt[0] != txt[-1]:
#         return False
#     return polindrom(txt[1:-1])

# myStr = input("Введите строку: ")
# print(polindrom(myStr))

# Шифрование
# def compress_recursive(string):
#     if len(string) == 0:
#         return []
#     elif len(string) == 1:
#         return [(string, 1)]
#     else:
#         compressed = compress_recursive(string[1:])
#         if string[0] == compressed[0][0]:
#             compressed[0] = (string[0], compressed[0][1] + 1)
#         else:
#             compressed.insert(0, (string[0], 1))
#         return compressed