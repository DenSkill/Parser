from classes.SuperJob import SuperJob


def main():
    # Создаем экземпляр класса Superjob для поиска вакансий на сайте superjob
    superjob = SuperJob()
    superjob.get_request("Pyton")
    superjob.print_info()


if __name__ == '__main__':
    main()

# x = SuperJob()
# keyword = input()
# x.get_request(keyword)
# Connector = x.getConnector(keyword) # когда создается Коннектор, через with open мы создаем фаил Connector
