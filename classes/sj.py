import requests
from classes.eng import Engine
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv('api_key')


class SuperJob(Engine):
    """Класс для парсинга вакансий с сайта SuperJob"""

    @staticmethod
    def _get_salary(salary_info: dict):
        """Обработка поля salary(зарплата)"""
        if salary_info.get('payment_to'):
            return salary_info['payment_to']
        if salary_info.get('payment_from'):
            return salary_info['payment_from']
        return 0

    @staticmethod
    def _get_remote_work(remote_work_info: dict):
        """Обработка поля remote_work(удаленная работа)"""
        if remote_work_info:
            if remote_work_info['id'] == 1:
                return 'В офисе'
            if remote_work_info['id'] == 2:
                return 'Удаленно'
        return 'Другое'

    def get_request(self, keyword):
        """Парсинг 500 вакансий и создание из них объекта типа list"""
        vacancies = []
        for page in range(5):
            response = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                    headers={'X-Api-App-Id': api_key},
                                    params={"keywords": keyword, "count": 100,
                                            "page": page}).json()
            for vacancy in response['objects']:
                vacancies.append({
                    "name": vacancy['profession'],
                    "company_name": vacancy['firm_name'],
                    "url": vacancy['link'],
                    "description": vacancy['candidat'],
                    "remote_work": self._get_remote_work(vacancy.get('place_of_work', {})),
                    "salary": self._get_salary(vacancy),
                })
        return vacancies
