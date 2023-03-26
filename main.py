from classes.SuperJob import SuperJob
import os
file_path = os.sep.join(["filename.json"])

def main():
    keyword = input("что ищем?")
    superjob = SuperJob()
    superjob.get_request(keyword)
    # connector = superjob.get_connector(file_path)
    # superjob.print_info()
    Connector = superjob.get_connector(keyword)# когда создается Коннектор, через with open мы создаем фаил Connector
    print(Connector)

if __name__ == '__main__':
    main()
