def print_menu():
    print("""
Меню :
1) Вывести список контактов.
2) Добавить контакт. 
3) Поиск.
4) Удалить контакт.""")


def print_data(lis):
    print("\nСписок контактов:\n")
    for i in lis:
        print(i.strip())
