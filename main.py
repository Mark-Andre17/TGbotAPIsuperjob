import datetime
import requests
from secret import *


def get_vacancies(dictionary):
    headers = {
        'X-Api-App-Id': secret_key,
        'Authorization': f"Bearer {token_dict['access_token']}",
    }
    url = 'https://api.superjob.ru/2.0/vacancies/'

    response = requests.get(url, headers=headers, params=dictionary).json()
    result = response['objects']
    for vacancies in result:
        value = datetime.datetime.fromtimestamp(vacancies["date_published"])
        yield f'Компания:{vacancies["firm_name"]}\n' \
              f'Вакансия:{vacancies["profession"]}\n' \
              f'Зарплата от:{vacancies["payment_from"]}\n' \
              f'Дата публикации:{value.strftime("%d-%m-%Y %H:%M:%S")}\n' \
              f'Ссылка:{vacancies["link"]}'



