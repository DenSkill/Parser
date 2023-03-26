import json


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
    def data_file(self, value: str) -> None:
        """Установка файла"""
        self.__data_file = value
        self.__connect()

    def __connect(self) -> None:
        """Перезаписывает файл на [] или создает новый и записывает []"""
        with open(self.__data_file, 'w') as file:
            json.dump([], file)

    def insert(self, data: list) -> None:
        """Запись данных в файл с сохранением структуры и исходных данных"""

        with open(self.__data_file, 'r', encoding='UTF-8') as file:
            data_json = json.load(file)

        with open(self.__data_file, 'w', encoding='UTF-8') as file:
            json.dump(data_json + data, file, indent=2, ensure_ascii=False)

    def select(self, query: dict) -> list:
        """
        Выбор данных из файла с применением фильтрации
        query- словаря, в котором ключ - это поле для
        фильтрации, а значение - это искомое значение, если
        передан пустой словарь, возвращает все данные файла
        """
        result = []
        with open(self.__data_file) as f:
            data = json.load(f)

        if not query:
            return data

        for item in data:
            if all(item.get(key) == value for key, value in query.items()):
                result.append(item)

        return result

    def delete(self, query: dict) -> list | None:
        """
        Удаление записей из файла, которые соответствуют запросу,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        if not query:
            return

        with open(self.__data_file) as f:
            data = json.load(f)

        result = []
        for item in data:
            if not all(item.get(key) == value for key, value in query.items()):
                result.append(item)

        with open(self.__data_file, 'w') as file:
            json.dump(result, file)
