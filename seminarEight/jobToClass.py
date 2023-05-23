# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text)

# with open('example.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1])


# with open('example.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     while line:        
#         print(line[:-1])
#         line = file.readline()

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text=file.read()
#     print(text.splitlines())

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text=file.readlines()
#     print(text)

# with open('example.txt', 'w', encoding='utf-8') as file:
#     some_list = ['hello', 'world', 'how', 'are', 'you']
#     for el in some_list:
#         file.write(el + '\n')

# import json
# some_dict = {1:2,3:4}
# with open('example.json', 'w', encoding='utf-8')as file:
#     json.dump(some_dict, file)

# Задача 1. Пользователь вводит кол-во строк, затем сами строки. Нужно записать в новый текстовый файл все эти строки. Далее пользователь вводит символ, нужно найти кол-во этого символа в новом файле.

# lines = int(input('Введите количество строк: '))
# with open('text.txt', 'w', encoding='utf-8') as file:
#     for _ in range(lines):
#         file.write(input('введите строку: ') + '\n')

# tmp_symbol = input('Введите символ: ')
# with open('text.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.count(tmp_symbol))

# Задача 2. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8')as files:
#         line = files.read().splitlines()
#         for i in range(len(line)-lines, len(line)):
#             print(line[i])

# read_last(3, 'article.txt')

# Задача 3. Документ «article.txt» содержит следующий текст:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as files:
        text = files.read().replace('\n', ' ').split(' ')
        max=0
        for i in range(len(text)):
            if len(text[i])>max:
                max=len(text[i])
        for i in range(len(text)):
            if len(text[i])==max:
                print(text[i])

longest_words('article.txt')