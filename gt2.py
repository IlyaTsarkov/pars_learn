import requests
from bs4 import BeautifulSoup

url = 'https://github.com/marketplace?query=sort%3Apopularity-desc&type=apps'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
}


def get_apps():
    response = requests.get(url=url, headers=headers)

    bs = BeautifulSoup(response.text, 'lxml')

    titles = bs.find_all(class_='h4')

    n = 0
    for title in titles:
        app_title = title.text.strip()
        n += 1
        print(f"{n} - {app_title}")


def main():
    get_apps()


if __name__ == '__main__':
    main()

