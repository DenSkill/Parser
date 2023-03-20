import os
import json


# SUPERJOB_API_KEY='v3.r.137435730.a9295b17ded23e51444f3fc1a79e40774997cd33.a988c8b784760bbdd692d89a8fa986310accadf0'
# export, printenv

class Superjob:
    """Данный класс создает запрос на API Superjob.ru"""

    def get_request(self):
        vacancy_list = []
        headers = {'X-Api-App-Id': os.environ['SUPERJOB_API_KEY']}  # токен
        for item in range(50):
            request = request.get('https://api.superjob.ru/2.0/vacancies/',
                                  headers=headers,
                                  params={'keywords': 'Python developer', 'page': item}).json()['objects']
            for item2 in request:
                vacancy_list.append(item2)
        return vacancy_list
