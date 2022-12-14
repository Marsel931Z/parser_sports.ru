import requests
from bs4 import BeautifulSoup as bs
import pandas

URL_TEMPLATE = "https://www.sports.ru/topnews/"
URL_TEMPLATE2 = "https://www.sports.ru/topnews/?page="
FILE_NAME = "sport.csv"


def parser_sport_news(URL):
    results = {'href': [], 'text': []}

    for i in range(1,21):
        r = requests.get(f'{URL}{i}')
        print(r.status_code)
        soup = bs(r.text, "html.parser")
        vacancies_names = soup.find_all("p")
        for names in vacancies_names:
            results['href'].append(f"https://www.sports.ru/{names.a['href']}")
            results['text'].append(names.a.string)
    return results

df = pandas.DataFrame(data=parser_sport_news(URL_TEMPLATE2))
df.to_csv(FILE_NAME)

