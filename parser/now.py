import os
import psycopg2
import requests
from bs4 import BeautifulSoup
from loader import DATABASE_URL

def connect_to_db():

    conn = psycopg2.connect(
        host=f'{os.getenv("DATABASE_HOST")}',
        database=f'{os.getenv("DATABASE_NAME")}',
        user=f'{os.getenv("DATABASE_USERNAME")}',
        password=f'{os.getenv("DATABASE_PASSWORD")}'
    )
    return conn


def parser_asic():

    url = "https://ultramining.com/crypto-calc/bitcoin/"
    response = requests.get(url)

    asics = []

    soup = BeautifulSoup(response.content, "html.parser")
    asics = soup.find_all("div", {"class": "col-6 col-lg-3 form-group"})

    for i in asics:
        title = i.find('label').text
        print(title.split())


print(parser_asic())




    # asics_list = []
    #
    # for x in asics:
    #     asics_list += x.text.strip().split('\n')
    #
    # new_asics_list = []
    #
    # not_accept = ['', 'W', 'Mh/s', 'h/s', 'Gh/s', 'kh/s', 'Th/s']
    #
    # for y in asics_list:
    #     if y not in not_accept:
    #         new_asics_list.append(y)
    #
    # return new_asics_list
