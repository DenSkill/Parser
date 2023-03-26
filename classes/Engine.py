from abc import ABC, abstractmethod

from classes.Connector import Connector


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        """Запрос вакансий через API"""
        pass

    @staticmethod
    def get_connector(file_name: str) -> Connector:
        """ Возвращает экземпляр класса Connector """
        return Connector(file_name)
