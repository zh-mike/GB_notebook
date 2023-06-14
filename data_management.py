# Работа с файлом. Считывание, запись.

def read_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        my_list = file.readlines()
        return (my_list)


def write_data(my_list):
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.writelines(my_list)

