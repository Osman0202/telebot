import requests
from bs4 import BeautifulSoup

URL = 'https://remanga.org/'

# HEADERS = {
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'User agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

def get_html(url):
    reg = requests.get(url=url)
    return reg


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="jsx-90e99f157179bcf3 container")
    manga = []
    for item in items:
        info = item.find('div', class_='jsx-14222a50a34f969e').find('div').string.split(', ')
        card = {
            'title': item.find('div', class_='Vertical_card__Sxft_').find('a').string,
            'link': item.find('div', class_='Vertical_card__Sxft_').find('a').get('href')
        }
        manga.append(card)
    return manga



def parser():
    html = get_html(URL)
    if html.status_code == 200:
        manga = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            manga.extend(current_page)
        return manga
    else:
        raise Exception("Bad request!")

# html = get_html(URL)
# print(html.text)