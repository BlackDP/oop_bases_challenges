"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return data


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as file:
            data = csv.DictReader(file)
            csv_list = []
            for row in data:
                csv_list.append(row)
            return csv_list



if __name__ == '__main__':
    txt_data = FileHandler('./data/text.txt')
    print(txt_data.read())
    json_data = JSONHandler('./data/recipes.json')
    print(json_data.read())
    csv_data = CSVHandler('./data/user_info.csv')
    print(csv_data.read())
