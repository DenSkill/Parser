from utils.superjob import Superjob


def main():
    # Создаем экземпляр класса Superjob для поиска вакансий на сайте superjob
    superjob = Superjob()
    superjob.get_request("Pyton")
    superjob.print_info()


if __name__ == "__main__":
    main()
