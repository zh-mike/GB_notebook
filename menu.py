import data_management as dm
import print_in_ter as pri
import app


def main_menu():
    contacts_list = dm.read_data()
    while True:
        pri.print_menu()
        op = input("Введите номер варианта: ")
        match op:
            case "1":
                pri.print_data(contacts_list)
            case "2":
                contacts_list = app.add_user(contacts_list)
            case "3":
                app.search_data(contacts_list)
            case "4":
                app.del_data(contacts_list)
        dm.write_data(contacts_list)
