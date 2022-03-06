import requests
from bs4 import BeautifulSoup
import json

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) '
                  'Gecko/20100101 Firefox/96.0'
}


def get_apps():
    apps_github_dict = {}
    for x in range(28):
        url = f'https://github.com/marketplace?page={x}' \
              f'&q=sort%3Apopularity-desc&query=sort%3Apopularity-desc&type=apps'

        response = requests.get(url=url, headers=headers)

        with open('index.html', 'w') as file:
            file.write(response.text)

        with open('index.html') as file:
            item = file.read()

        bs = BeautifulSoup(item, 'lxml')

        titles = bs.find_all(class_='col-md-6 mb-4 d-flex no-underline')

        for title in titles:
            app_title = title.find('h3', class_='h4').text.strip()
            app_href = 'https://github.com/' + title.get("href")
            apps_github_dict[app_title] = app_href

    with open('apps_info_dict.json', 'w') as file:
        json.dump(apps_github_dict, file, indent=4)


def main():
    get_apps()


if __name__ == '__main__':
    main()






