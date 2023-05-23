# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random
N = int(input("Введите длину списка: "))
some_list = []
for _ in range(N):
    some_list.append(int(input()))
print(some_list)
X = int(input('Введите число Х: '))
print(some_list.count(X))

a = [int(input()) for _ in range(int(input()))]
x = int(input())
print(a.count(x))


# Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны
# N целых чисел Ai. Последняя строка содержит число X.

X = int(input('Введите число Х: '))
N = int(input("Введите длину списка: "))
some_list = []
temp = 0
for i in range(N):
    some_list.append(int(input()))
    if 0 <= X-some_list[i] <= X-temp:
        temp = i
print(f'Исходный список - {some_list}')
print(
    f'Самый близкий по величине элемент к заданному числу {X} равен {some_list[temp]}')

rnd_list = [random.randint(-100, 100) for _ in range(10)]
x = int(input())
some_set = set(some_list)
diff = 0
while True:
    if x+diff in some_set:
        print(x+diff)
        break
    elif x-diff in some_set:
        print(x-diff)
        break
    diff += 1

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае
# с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на
# вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

dict_1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
          'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'D': 2,
          'G': 2, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'B': 3, 'C': 3, 'M': 3,
          'P': 3, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4,
          'Y': 4, 'Й': 4, 'Ы': 4, 'K': 5, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'J': 8,
          'X': 8, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Q': 10, 'Z': 10, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
str = input('Введите слово: ').upper()
print(sum([value for i in str for key, value in dict_1.items() if i in key]))