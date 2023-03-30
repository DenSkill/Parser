import requests
from classes.eng import Engine


class HeadHunter(Engine):
    """Класс для парсинга вакансий с сайта HeadHunter"""

    @staticmethod
    def _get_salary(salary_info: dict):
        """Обработка поля salary(зарплата): предпочтительно выводить зарплату 'от', если же она не указана,
                то выводить зарплату 'до'. Или выводить 0, если поле отсутствует"""
        if salary_info:
            if salary_info.get('to'):
                return salary_info['to']
            if salary_info.get('from'):
                return salary_info['from']
        return 0

    @staticmethod
    def _get_remote_work(remote_work_info: dict):
        """Обработка поля remote_work(удаленная работа)"""
        if remote_work_info:
            if remote_work_info['id'] == 'fullDay':
                return 'В офисе'
            if remote_work_info['id'] == 'remote':
                return 'Удаленно'
        return 'Другое'

    def get_request(self, keyword):
        """Парсинг 500 вакансий и создание из них объекта типа list"""
        vacancies = []
        for page in range(5):
            response = requests.get(f"https://api.hh.ru/vacancies?text={keyword}",
                                    params={'per_page': '100', 'page': page}).json()
            for vacancy in response['items']:
                vacancies.append({
                    "name": vacancy['name'],
                    "company_name": vacancy['employer']['name'],
                    "url": vacancy['alternate_url'],
                    "description": vacancy['snippet']['requirement'],
                    "remote_work": self._get_remote_work(vacancy.get('schedule', {})),
                    "salary": self._get_salary(vacancy.get('salary', {})),
                })
        return vacancies
