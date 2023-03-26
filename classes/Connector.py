import json
import os


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, file_path: str):
        self.__data_file = file_path
        self.__connect()

    @property
    def data_file(self) -> str:
        return self.__data_file

    @data_file.setter
    def data_file(self, value: str):
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        with open(self.__data_file, 'r', encoding='UTF-8') as file:
            json_reader = json.load(file)
            print(len(json_reader))

    def insert(self, data: list) -> None:
        """Запись данных в файл с сохранением структуры и исходных данных"""
        pass

    def select(self, query: dict) -> list:
        """
        Выбор данных из файла с применением фильтрации
        query- словаря, в котором ключ - это поле для
        фильтрации, а значение - это искомое значение, если
        передан пустой словарь, возвращает все данные файла
        """
        pass

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запросу,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        pass
