# Основные функции
import time
from print_in_ter import *

def add_note(data):
    new_note = {
        'id': str(int(data['notes'][-1]['id']) + 1),
        'title': input("Введите заголовок заметки: "),
        'text': input("Введите тело заметки: "),
        'time': time.strftime('%y.%m.%d')
    }
    data['notes'].append(new_note)
    print("Заметка успешно добавлен")
    return data


def search_data(data):
    search = input("Что ищем? ")
    flag = 0
    print()
    for el in data['notes']:
        if search in el.values():
            print_note(el)
            flag += 1
    if flag == 0:
        print("Нет совпадений")


def del_data(data):
    flag = 0
    search = input("Выберите заметку: ")
    print()
    while True:
        for el in data['notes']:
            if search in el.values():
                print_note(el)
                del_user = el
                flag += 1
        if flag > 1:
            search = input("Уточните какую именно заметку вы хотите удалить?: ")
            flag = 0
            continue
        if flag == 0:
            print("Нет совпадений")
            return
        if flag == 1:
            confirm = input(f"Удалить заметку?\n"
                            f"1) Удалить\n"
                            f"2) Вернуться в меню\n")
            match confirm:
                case "1":
                    data['notes'].remove(del_user)
                    print(f"Заметка успешно удалена")
                    return
                case _:
                    return
