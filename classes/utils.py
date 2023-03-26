#классы для фильтрации списков вакансий

def sorting(vacancies):
    """Сортирует список вакансий по ежемесячной оплате"""
    sorted_by_salary = sorted(vacancies, key=lambda v: v.salary, reverse=True)
    return sorted_by_salary