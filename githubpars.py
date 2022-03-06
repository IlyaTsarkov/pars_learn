import requests
from bs4 import BeautifulSoup


url = 'https://github.com/marketplace?query=sort%3Apopularity-desc&type=apps'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
}


def get_apps():
    response = requests.get(url=url, headers=headers)

    # bs = BeautifulSoup(src, "lxml")
    # apps_cards = bs.find_all("div", class_="d-md-flex flex-wrap mb-4")

    with open('index.html') as file:
        item = file.read()

    bs = BeautifulSoup(item, "lxml")

    # apps_cards = bs.find_all("div", class_="d-md-flex flex-wrap mb-4")

    apps_titles = bs.find_all(class_='h4')
    # n = 0
    # for app_card in apps_cards:
    #     app_name = app_card.find("div", class_="px-3").text.strip()
    #     # app_count_of_installs = app_card.find("span", class_="text-small color-fg-muted text-bold").text.strip()
    #
    #     print(app_card)
    #     print(f"{app_name}")
    #     print(n)

    for app_title in apps_titles:
        app_text_title = app_title.text.strip()
        print(app_text_title)


def main():
    get_apps()


if __name__ == '__main__':
    main()
