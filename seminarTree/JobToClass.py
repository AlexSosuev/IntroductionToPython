# Задача 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

import random
n = int(input("Введите длину списка: "))
some_list = []
for _ in range(n):
    some_list.append(random.randint(1, 100))
print(some_list)
print(len(set(some_list)))


# Задача 19. Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

n = int(input("Введите длину списка: "))
some_list = []
for _ in range(n):
    some_list.append(random.randint(1, 100))
print(some_list)
k = int(input("Введите сдвиг: "))
new_list = []
new_list.extend(some_list[k:len(some_list)])
new_list.extend(some_list[:k])
print(new_list)

# Задача 21. Напишите программу для печати всех уникальных значений в словаре.

dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
          {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]
unique_value = set()
for item in dict_1:
    unique_value.add(list(item.values())[0].strip())
print(sorted(unique_value))

# Задача 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)

n = int(input("Введите длину списка: "))
some_list = []
for _ in range(n):
    some_list.append(random.randint(-10, 10))
print(some_list)
k = 0
for i in range(len(some_list)-1):
    if some_list[i] < some_list[i+1]:
        k += 1
print(f'k = {k}')
