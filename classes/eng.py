from abc import ABC, abstractmethod

from classes.cnctr import Connector


class Engine(ABC):
    """Абстрактный класс для парсинга вакансий"""

    @abstractmethod
    def get_request(self, keyword):
        """Запрос информации с сайта по ключевому слову"""
        pass

    @staticmethod
    def get_connector(file_name):
        """Возвращает экземпляр класса Connector для работы с записанной в файл json информацией о вакансиях"""
        connector = Connector(file_name)
        return connector

    def save_vacancies(self, file_name, vacancies):
        """Сохраняет собранные с сайтов вакансии в файл json"""
        connector = self.get_connector(file_name)
        connector.insert(vacancies)
