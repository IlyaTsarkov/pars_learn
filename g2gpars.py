import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) '
                  'Gecko/20100101 Firefox/96.0'
}


def get_sellers():
    url = 'https://www.g2g.com/offer/Dragon-s-Call-TBC--DE----' \
          'Alliance?service_id=lgc_service_1&brand_id=lgc_game_29076&region' \
          '_id=ac3f85c1-7562-437e-b125-e89576b9a38e&fa=lgc_29076_server%3Algc_' \
          '29076_server_40988&q=dra&sort=lowest_price&include_offline=1'

    response = requests.get(url=url, headers=headers)

    with open('index_g2g.html', 'w') as file:
        file.write(response.text)

    with open('index_g2g.html') as file:
        item = file.read()

    bs = BeautifulSoup(item, 'lxml')

    sellers = bs.find_all(class_='other_offer-desk-main-box other_offer-div-box')

    for seller in sellers:
        seller_name = seller.find("div", class_='seller__name-detail').text.strip()
        seller_stock = seller.find("div", class_='offers-bottom-attributes '
                                                 'offer__content-lower-items').find_next().find_next(
        ).find("span").text.strip()
        seller_price = seller.find("span", class_='offer-price-amount').text

        print(f"{seller_name} - {seller_stock} - {seller_price}")


def main():
    get_sellers()


if __name__ == '__main__':
    main()



