import requests

from classes.Engine import Engine


class HH(Engine):
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self, search: str, experience=None):
        """Инициализируется запросом пользователя"""
        self.params = {'text': f'{search}', 'page': 0, 'per_page': 100}
        if experience is not None:
            self.params['experience'] = experience

    @staticmethod
    def get_format_date(date: str) -> str:
        """Возвращает отформатированную дату"""
        date_format = datetime.datetime.fromisoformat(date).strftime("%d.%m.%Y %X")
        return date_format

    def get_request(self):
        """Запрос вакансий через API"""
        try:
            response = requests.get(self.URL, self.params)
            if response.status_code == 200:
                return response.json()

        except requests.RequestException:
            print('Не удается получить данные')

    def get_info_vacancy(self, data: dict) -> dict:
        """Получаем информацию о вакансии"""
        info = {
            'source': 'HeadHunter',
            'name': data['name'],
            'url': data['alternate_url'],
            'description': data.get('snippet').get('responsibility'),
            'salary': data.get('salary'),
            'date_published': self.get_format_date(data['published_at'])
        }
        return info

    def get_vacancies(self) -> list:
        """Получаем информацию о вакансии для дальнейшей записи в файл и создания экземпляров Vacancy"""
        vacancies = []
        page = 0
        while True:
            self.params['page'] = page
            data = self.get_request()
            for vacancy in data.get('items'):
                if vacancy.get('salary') is not None and vacancy.get('salary').get('currency') is not None:
                    # если зп рубли, добавляем в список, если нет, пропускаем
                    if vacancy.get('salary').get('currency') == "RUR":
                        vacancies.append(self.get_info_vacancy(vacancy))
                    else:
                        continue

                # если зп не указана, добавляем в список
                else:
                    vacancies.append(self.get_info_vacancy(vacancy))

            if data.get('found') == len(vacancies):
                break

            elif len(vacancies) >= 500:
                break

            else:
                page += 1

        return vacancies
