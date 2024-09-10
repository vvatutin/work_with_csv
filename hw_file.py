'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
Домашнее задание:
Дополнить справочник возможностью копирования данных из одного файла в другой.
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
Формат сдачи: ссылка на свой репозиторий.
'''
from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'
file_double = 'double.csv'


def get_info():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер')
    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'имя': lst[0], 'фамилия': lst[1], 'телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def copy_file(file_name):
    num_str = int(input('Введите номер строки, которую нужно скопировать: '))
    res = read_file(file_name)
    if num_str <= len(res):
        if not exists(file_double):
            create_file(file_double)
        with open(file_double, 'w', encoding='utf-8', newline='') as data_double:
            f_w = DictWriter(data_double, fieldnames=['имя', 'фамилия', 'телефон'])
            f_w.writeheader()
            f_w.writerow(res[num_str - 1])
        print(*read_file(file_double))
    else:
        print("Вы ввели номер строки, превышающий число строк в файле")


def row_search(file_name):
    last_name = input("Введите фамилию: ")
    res = read_file(file_name)
    for elem in res:
        if elem["фамилия"] == last_name:
            return elem


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == "s":
            print(row_search(file_name))
        elif command == "c":
            copy_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            print(*read_file(file_name))


main()
