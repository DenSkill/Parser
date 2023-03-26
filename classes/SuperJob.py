import requests

from classes.Engine import Engine
import os


SUPERJOB_API_KEY='v3.r.137435730.a9295b17ded23e51444f3fc1a79e40774997cd33.a988c8b784760bbdd692d89a8fa986310accadf0'
# export, printenv


class SuperJob(Engine):
    """Данный класс создает запрос на API Superjob.ru"""

    def get_request(keyword):
        vacancy_list = []
        #headers = {'X-Api-App-Id': os.environ['SUPERJOB_API_KEY']}
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        for item in range(2):
            response = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                    headers=headers,
                                    params={'keywords': keyword, 'page': item}).json()['objects']
            vacancy_list.extend(response)
            print(1)
        return vacancy_list


keyword = "Python"  # через инпут
x = SuperJob
x.get_request(keyword)
