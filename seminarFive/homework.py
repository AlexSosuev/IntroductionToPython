# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def step(a, b):
    if b == 0 or a == 1:
        return 1
    return a * step(a, b - 1) if b > 0 else 1/(a * step(a, b + 1))


a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", step(a, b))

# Задача 6. Дана строка (возможно, пустая), состоящая из букв A-Z:

# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB.

# Нужно написать функцию RLE, которая на выходе даст строку вида:

# A4B3C2XYZD4E3F3A6B28

# И сгенерирует ошибку, если на вход пришла невалидная строка.

# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется
# количество повторений.

from string import ascii_letters
def rle(input_string):
    encoded_string = ""
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] not in ascii_letters:
            return 'Введена невалидная строка!!!'
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + (str(count) if count > 1 else "")
            count = 1

    if count > 0:
        encoded_string += input_string[-1] + (str(count) if count > 1 else "")

    return encoded_string

input_string = "AAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBB"
print(rle(input_string))
input_string = "AAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBB1111111"
print(rle(input_string))
