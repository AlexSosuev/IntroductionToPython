# Задача 25. Напишите программу, которая принимает на вход строку,
# и выводит кол-во повторов каждого из символов 1 раз.
# import time
# import random

# some_str = ''.join([chr(random.randint(32, 100)) for _ in range(10 ** 5)])

# start = time.perf_counter()
# for letter in set(some_str):
#     a = letter, some_str.count(letter)
# end = time.perf_counter()
# duration1 = end - start

# start = time.perf_counter()
# for letter in set(some_str):
#     amount = 0
#     for letter1 in some_str:
#         if letter == letter1:
#             amount += 1
#     a = letter, amount
# end = time.perf_counter()
# duration2 = end - start
# # print(duration2 / duration1)

# start = time.perf_counter()
# count = 0
# lens = len(some_str)
# while lens > 0:
#     for i in range(0, lens):
#         if some_str[0] == some_str[i]:
#             count += 1
#     lens -= count
#     a = f'{some_str[0]} -> {count}'
#     some_str = some_str.replace(some_str[0], '')
#     count = 0
# end = time.perf_counter()
# duration3 = end - start


# start = time.perf_counter()
# count_dict = {}  # a: 1
# for letter in some_str:
#     if letter not in count_dict:
#         count_dict[letter] = 1
#     else:
#         count = count_dict[letter]
#         count_dict[letter] = count + 1
# end = time.perf_counter()
# duration4 = end - start
# print(duration1, duration2, duration3, duration4)


# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте. без метода split()

str5 = '''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells'''

some_str = str5.lower().split()
print(len(set(some_str)))

temp_word = ''
some_set = set()
for letter in str5:
    if letter != ' ':
        temp_word += letter
    else:
        if temp_word:
            some_set.add(temp_word)
            temp_word = ''
some_set.add(temp_word)
print(len(some_set))


# set_test = set()
# temp_str = ""
# for i in str5.lower():
#     if i == " " or i == '.' or i == '\n':
#         if temp_str != "":
#             set_test.add(temp_str)
#         temp_str = ""
#     else:
#         temp_str += i

# print(len(set_test))


# import re
# def rle(input_string):
#     if not re.match("^[A-Z]*$", input_string):
#         raise ValueError("Invalid input string")

#     encoded_string = ""
#     count = 1

#     for i in range(1, len(input_string)):
#         if input_string[i] == input_string[i - 1]:
#             count += 1
#         else:
#             encoded_string += input_string[i - 1] + (str(count) if count > 1 else "")
#             count = 1

#     if count > 0:
#         encoded_string += input_string[-1] + (str(count) if count > 1 else "")

#     return encoded_string


# input_string = "AAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBB"
# print(rle(input_string))

# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние
# по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

# l2 = [1, 4, 5, 2, 3, 9, 8, 11, 0]
# l2.sort()
# print(l2)
# for i in range(len(l2)-1):
#     if l2[i+1] == l2[i]+1:
