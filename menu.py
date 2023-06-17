import data_management as dm
import print_in_ter as pri
import app


def main_menu():
    data = dm.read_data()
    while True:
        pri.print_menu()
        op = input("Введите номер варианта: ")
        match op:
            case "1":
                pri.print_data(data)
            case "2":
                data = app.add_note(data)
            case "3":
                app.search_data(data)
            case "4":
                app.del_data(data)
        dm.write_data(data)

