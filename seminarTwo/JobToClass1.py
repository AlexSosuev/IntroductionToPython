# Вводятся числа, пока не введут 0. Найти сумму четных чисел

# a = [1, 2, 3, 4, -5]
# ind = 0
# while x := input() != 0:
#     if a[ind] < 0:
#         print('YES')
#         break
#     ind += 1
# else:
#     print('No')

# Значение переменной-итератера используется
# for i in range(1, 11):
#     print(i ** 2)


# Значение переменной-итератера не используется
# for _ in range(100, 110, 2):  # 0, 1, 2, 3, 4
#     print('HELLO')

# some_list = [-3, 4, 5, 0, 1]
# for a in some_list:
#     print(a)
#
# for ind in range(0, len(some_list)):  # 0, 1, 2, 3, 4
#     print(some_list[ind])


# a = []
# a.append(10)
# print(a)
#
#
# a = []
# print(a)
# a[1] = 200
# a[2] = 300
# print(a)
# Вводятся числа, пока не введут 0. Найти сумму четных чисел

# a = [1, 2, 3, 4, -5]
# ind = 0
# while ind < len(a):
#     if a[ind] < 0:
#         print('YES')
#         break
#     ind += 1
# else:
#     print('No')

# Значение переменной-итератера используется
# for i in range(1, 11):
#     print(i ** 2)


# Значение переменной-итератера не используется
# for _ in range(100, 110, 2):  # 0, 1, 2, 3, 4
#     print('HELLO')

# some_list = [-3, 4, 5, 0, 1]
# for a in some_list:
#     print(a)
#
# for ind in range(0, len(some_list)):  # 0, 1, 2, 3, 4
#     print(some_list[ind])


# a = []
# a.append(10)
# print(a)
#
#
# a = []
# print(a)
# a[1] = 200
# a[2] = 300
# print(a)

# Вводится 2 числа a и b Найти все простые число в дипапзоне от a до b
a = int(input())
b = int(input())
for i in range(a, b + 1):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        print(i)
