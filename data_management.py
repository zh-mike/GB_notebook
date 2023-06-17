# Работа с файлом. Считывание, запись.
import json


def read_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data


def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
