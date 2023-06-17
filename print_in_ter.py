import json


def print_menu():
    print("""
Меню :
1) Вывести список заметок.
2) Добавить заметку. 
3) Поиск.
4) Удалить заметку.""")


def print_data(data):
    print("\nСписок заметок:\n")
    for note in data['notes']:
        print(note["title"])
        print(note["text"])
        print(note['time'])
        print()