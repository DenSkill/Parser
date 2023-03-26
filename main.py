from classes.SuperJob import SuperJob


def main():
    # Создаем экземпляр класса Superjob для поиска вакансий на сайте superjob
    keyword = input("что ищем?")
    superjob = SuperJob()
    superjob.get_request(keyword)
    # superjob.print_info()
    Connector = superjob.get_connector(keyword)# когда создается Коннектор, через with open мы создаем фаил Connector
    print(Connector)

if __name__ == '__main__':
    main()
