import json
from classes.sj import SuperJob
from classes.hh import HeadHunter
from classes.vac import Vacancy

# Запрос у пользователя ключевого слова, по которому будет производиться поиск.
word_for_search = input('Введите ключевое слово для поиска: ')

# парсинг 500 вакансий по заданному слову с сайта HeadHunter и сохранение их в файл vacancies_list.json
h = HeadHunter()
response = h.get_request(word_for_search)
into_file_hh = h.save_vacancies('vacancies_list.json', response)

# парсинг 500 вакансий по заданному слову с сайта SuperJob и добавление их в тот же файл vacancies_list.json
s = SuperJob()
response = s.get_request(word_for_search)
into_file_sj = s.save_vacancies('vacancies_list.json', response)

# вывод меню для пользователя
print('По вашему запросу собрано 500 вакансий с сайта SuperJob и 500 вакансий с сайта HeadHunter.\nВыберите '
      "дальнейшее действие:\nВывести список всех вакансий: нажмите s\nВывести 10 самых высокооплачиваемых вакансий: "
      "нажмите t\nВывести вакансии с возможностью удаленной работы: нажмите n\nЕсли вы хотите завершить программу: "
      "нажмите z")

# чтение общего списка вакансий спарсенных с двух сайтов
with open('vacancies_list.json', 'r', encoding='utf8') as f:
    vacancies_from_json = json.load(f)
    vacancy_subjects = []
    for vac in vacancies_from_json:
        v = Vacancy(vac["name"], vac["company_name"], vac["url"], vac["description"], vac["remote_work"], vac["salary"])
        vacancy_subjects.append(v)

# выбор пользователем варианта из меню
user_choice = input()

while user_choice != 'z':
    if user_choice == 's':
        # вывод списка всех вакансий
        for i in vacancy_subjects:
            print(i)
        user_choice = input('Введите следующую команду ')
    if user_choice == 't':
        # вывод 10 самых высокооплачиваемых вакансий
        sorted_vacancies = sorted(vacancy_subjects, reverse=True)[:10]
        for i in sorted_vacancies:
            print(i)
        user_choice = input('Введите следующую команду ')
    if user_choice == 'n':
        # вывод вакансий с возможностью удаленной работы
        remote_vacancies = []
        for i in vacancy_subjects:
            if i.remote_work == 'Удаленно':
                remote_vacancies.append(i)
        for rem in remote_vacancies:
            print(rem)
        user_choice = input('Введите следующую команду ')
    else:
        # обработка неверного значения, введенного пользователем
        print('Вы ввели неверное значение. Пожалуйста, попробуйте еще раз или нажмите z для завершения программы')
        user_choice = input()

print('Программа завершена')
