# Функция чтение всего файла
def view_file(file):
    with open(file, 'r', encoding='utf-8') as phone:
        return phone.read()

# Функция записи в справочник
def write_file(file):
    with open(file, 'a', encoding='utf-8') as phone:
        record = get_info()
        phone.write(f'{record[0]} {record[1]} {record[2]} {record[3]}')
        print('Контакт добавлен')

# Функция создания записи для справочника
def get_info():
    info = []
    info.append('\n' + input('Введите фамилию: '))
    info.append(input('введите имя: '))
    info.append(input('введите отчество: '))
    info.append(input('Введите номер телефона: '))
    return info

# Функция поиска записи
def find_record(fragment, file):
    with open(file, 'r', encoding='utf-8') as phone:
        while True:
            line = phone.readline()
            if not line:
                break
            if line.find(fragment)  != -1:
                print(line[:-1])

# Выбор режима работы со справочником
def interface():
    file = 'phonebook.txt'
    mode = int(input('Введите режим работы со справочником: \n\tчтение справочника - 1 \n\tдобавление записи в справочник - 2 \n\tпоиск записи - 3\n'))
    match mode:
        case 1:
            print(view_file(file))
        case 2:
            write_file(file)
        case 3:
            fragment = input('Кого будем искать: ')
            find_record(fragment, file)
        case _:
            print('Вы ввели некорректный режим работы!!!')

interface()