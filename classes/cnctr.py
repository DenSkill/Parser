import json
import os
from datetime import datetime


class JSONDegaradationException(Exception):
    """Класс обработки ошибки в случае деградации файла"""

    def __init__(self, *args):
        self.message = args[0] if args else 'Файл потерял актуальность в структуре данных'

    def __str__(self):
        return self.message


class Connector:
    """Класс коннектор к файлу в json формате"""

    __data_file = None

    def __init__(self, filename):
        self.data_file = filename

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """Проверка на существование файла с данными и создание его при необходимости. Проверка на деградацию"""
        with open(self.__data_file, 'a+', encoding='utf8') as f:
            f.seek(0)
            first_line = f.readline()
            if first_line:
                try:
                    f.seek(0)
                    data = json.load(f)
                    assert type(data) == list
                    for item in data:
                        assert type(item["name"]) == str
                        assert type(item["company_name"]) == str
                        assert type(item["url"]) == str
                        assert type(item["remote_work"]) == str
                        assert type(item["salary"]) == int
                except:
                    raise JSONDegaradationException()
            else:
                json.dump([], f)
        # Проверка на актуальность файл по времени
        if (datetime.now() - datetime.fromtimestamp(os.path.getmtime(self.__data_file))).days >= 1:
            raise JSONDegaradationException()

    def insert(self, data):
        """Запись данных в файл, если файл пустой. Добавление данных в файл, если в нем есть данные"""
        with open(self.__data_file, 'r', encoding='utf8') as f:
            file_data = json.load(f)

        if type(data) == dict:
            file_data.append(data)
        elif type(data) == list:
            file_data.extend(data)

        with open(self.__data_file, 'w', encoding='utf8') as f:
            json.dump(file_data, f, ensure_ascii=False, indent=4)

    def select(self, query):
        """Выбор данных из файла с применением фильтрации"""
        search_key, search_value = query.items()[0]

        with open(self.__data_file, 'r', encoding='utf8') as f:
            file_data = json.load(f)

        result = []
        for vacancy in file_data:
            if vacancy[search_key] == search_value:
                result.append(vacancy)
        return result

    def delete(self, query):
        """Удаление записей из файла, которые соответствуют запросу"""
        if not query:
            return

        del_key, del_value = list(query.items())[0]

        with open(self.__data_file, 'r', encoding='utf8') as f:
            file_data = json.load(f)

        non_del = []
        for vacancy in file_data:
            if vacancy[del_key] == del_value:
                pass
            else:
                non_del.append(vacancy)

        with open(self.__data_file, 'w', encoding='utf8') as f:
            json.dump(non_del, f, ensure_ascii=False, indent=4)
