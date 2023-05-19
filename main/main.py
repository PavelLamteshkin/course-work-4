from classes import HeadHunterAPI, SuperJobAPI, JSONSaver
from utils import sort_by_salary_min


def main():

    keyword = input('По какому ключевому слову ищем вакансию: ')
    platforms = input(f'HeadHunter или SuperJob? ')
    count = int(input('Сколько вакансий смотрим? '))

    if platforms == 'HeadHunter':
        hh_api = HeadHunterAPI() # Создание экземпляра класса для работы с API HeadHunter
        hh_vacancies = hh_api.get_vacancies(keyword, count) # Получение вакансий с HeadHunter

        # Сохранение информации о вакансиях HeadHunter в файл
        json_saver = JSONSaver(keyword)
        json_saver.add_vacancies(hh_vacancies)

        data = json_saver.select_HH()
        data = sort_by_salary_min(data)

    elif platforms == 'SuperJob':
        superjob_api = SuperJobAPI() # Создание экземпляра класса для работы с API SuperJob
        superjob_vacancies = superjob_api.get_vacancies(keyword, count) # Получение вакансий с SuperJob

        # Сохранение информации о вакансиях SuperJob в файл
        json_saver = JSONSaver(keyword)
        json_saver.add_vacancies(superjob_vacancies)

        data = json_saver.select_SJ()
        data = sort_by_salary_min(data)

    else:
        print('Ошибка в имени платформы.')


    for row in data:
        print(row, end=f'\n{"*" * 30}\n')

    json_saver.delete_vacancy()


if __name__ == "__main__":
    main()
