# Задача №31. Решение в группах Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1,
# ak  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи.

# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n - 1) + fib(n - 2)

# def fib_while(n):
#     first = 0
#     second = 1
#     temp_number = first + second
#     count = 2
#     while count < n:
#         first, second = second, temp_number
#         temp_number = first + second
#         count += 1
#     print(temp_number)


# print(fib_while(int(input('please enterthe number of Fibbonachi: '))))


# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# amount_of_list = int(input())
# some_list = [int(input()) for _ in range(amount_of_list)]
# print(some_list)

# max_value = max(some_list)
# min_value = min(some_list)

# for i in range(len(some_list)):
#     if some_list[i] == max_value:
#         some_list[i] = min_value

# print(some_list)

# def reverse(n, list1):
#     if n <= 0:
#         #print(list1[0], end=' ')
#         return list1[0]
#     else:
#         print(list1[n-1], end=' ')
#         return reverse(n - 1, list1)


# reverse(6, [11, 21, 31, 41, 51, 61])

# Задача 5.
# numbers = [1, 4, 6, 2, 3, 9, 8, 11, 0]
# sort = sorted(set(numbers))
# ranges = []
# start = sort[0]
# end = start

# for i in range(1, len(sort)):
#     if sort[i] == end + 1:
#         end = sort[i]
#     else:
#         if start == end:
#             ranges.append(str(start))
#         else:
#             ranges.append(f"{start}-{end}")
#         start = end = sort[i]

# if start == end:
#     ranges.append(str(start))
# else:
#     ranges.append(f"{start}-{end}")

# print(",".join(ranges))

# Задача3
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]

# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".

# sample_input = ["eat", "bat", "tea", "tan", "ate", "nat"]

# x = {}

# for elem in sample_input:
#     sorted_el = ''.join(sorted(elem))
#     if sorted_el in x:
#         x[sorted_el].append(elem)
#     else:
#         x[sorted_el] = [elem]

# print(list(x.values()))

# Задача 5_1
# some_list = [1, 4, 3, 9, 8, 11, 0, 13]
# some_list.sort()
# result_list = []
# temp_list = []
# print(some_list)
# for i in range(0, len(some_list) - 1):
#     if some_list[i + 1] - some_list[i] == 1:
#         temp_list.append(some_list[i])
#     else:
#         temp_list.append(some_list[i])
#         result_list.append(temp_list)
#         temp_list = []
# if temp_list:
#     result_list.append(temp_list)

# if some_list[-1] - some_list[-2] == 1:
#     result_list[-1].append(some_list[-1])
# else:
#     result_list.append([some_list[-1]])

# print(result_list)
# print_list = []
# for i in result_list:
#     if len(i) > 1:
#         print_list.append(f'{i[0]}-{i[-1]}')
#     else:
#         print_list.append(i[0])
# print(*print_list, sep=',')

# Задача 6
import re


def rle(input_string):
    if not re.match("^[A-Z]*$", input_string):
        raise ValueError("Invalid input string")

    encoded_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + \
                (str(count) if count > 1 else "")
            count = 1

    if count > 0:
        encoded_string += input_string[-1] + (str(count) if count > 1 else "")

    return encoded_string


input_string = "AAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBB"
print(rle(input_string))
