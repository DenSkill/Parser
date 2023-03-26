import data as data
import requests

from classes.Engine import Engine
import os

SUPERJOB_API_KEY = 'v3.r.137435730.a9295b17ded23e51444f3fc1a79e40774997cd33.a988c8b784760bbdd692d89a8fa986310accadf0'


# export, printenv


class SuperJob(Engine):
    """Данный класс создает запрос на API Superjob.ru"""
    def __init__(self, keyword):
        self.keyword = keyword # Слово, по которому мы ищем

    def get_request(self, keyword):
        vacancy_list = []
        # headers = {'X-Api-App-Id': os.environ['SUPERJOB_API_KEY']}
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        for item in range(2):
            response = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                    headers=headers,
                                    params={'keywords': keyword, 'page': item}).json()['objects']
            vacancy_list.extend(response)
            # print(1) # test
        return vacancy_list

    def get_info_vacancy(self, data: dict) -> dict:
        """Получаем информацию о вакансии"""
        salary = {'from': data['payment_from'],
                  'to': data['payment_to'],
                  'currency': data['currency']}
        info = {
            'source': 'SuperJob',
            'name': data['profession'],
            'url': data['link'],
            'description': data.get('client').get('description'),
            'salary': salary,
            'date_published': self.get_format_date((data['date_published'])),
        }
        return info

  #  def get_vacancies(self) -> list:
  #      """Получает список всех вакансий"""
  #      vacancies = []
  #      for i in range(1):
  #          self.params['page'] = i
 #           data = self.get_request()
 #           for vacancy in data.get('objects'):
 #               if vacancy.get('currency') is not None:
 #                   if vacancy.get('currency') == "rub":
 #                       vacancies.append(self.get_info_vacancy(vacancy))
 #                   else:
 #                       continue
 #           if len(vacancies) >= 500:
 #               break
 #       return vacancies

#keyword = input("что ищем?")
keyword = 'Python'
superjob = SuperJob(keyword)
print(superjob.get_connector(keyword))
#Connector = superjob.get_connector(keyword)# когда создается Коннектор, через with open мы создаем фаил Connector
#print(Connector)
