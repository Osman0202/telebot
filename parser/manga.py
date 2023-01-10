import requests
from bs4 import BeautifulSoup

class ParserManga:
    __URL = 'https://remanga.org/'

    __HEADERS = {
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
         'User agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}



    @classmethod
    def __get_html(cls, url=None):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)
        return req
    @staticmethod
    def __get_data(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_="jsx-14222a50a34f969e")
        manga = []
        for item in items:
            # info = item.find('div', class_='jsx-14222a50a34f969e').find('div').string.split(', ')
            card = {
                'title': item.find('div', class_='Vertical_card__Sxft_').find('a').string,
                'link': item.find('div', class_='Vertical_card__Sxft_').find('a').get('href')
            }
            manga.append(card)
        return manga



    @classmethod
    def parser(cls):
        html = cls.__get_html()
        if html.status_code == 200:
            manga = []
            for i in range(1, 2):
                html = cls.__get_html(f"{cls.__URL}page/{i}/")
                current_page = cls.__get_data(html.text)
                manga.extend(current_page)
            return manga
        else:
            raise Exception("Bad request!")

    # html = get_html(URL)
    # print(html.text)