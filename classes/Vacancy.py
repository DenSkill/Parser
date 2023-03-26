class Vacancy:
    def __init__(self, name='', description='', salary='', service=''):
        self.service = service
        self.name = name
        self.description = description
        self.salary = salary

    def __str__(self):
        return f'{self.service} name:{self.name}, {self.title}, {self.salary}, {self.description}'