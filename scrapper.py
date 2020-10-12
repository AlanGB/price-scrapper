import requests
import lxml.html as html
import csv

MEDICAMENTOS_URL = 'https://www.fahorro.com/medicamentos.html'
XPATH_LINKS_TO_CATALOGUES = '//dl[@id="narrow-by-list"]/dd[1]/ol/li/a/@href'
XPATH_PRODUCT_NAME = '//ul/li/div/h2/a/text()'
XPATH_PRODUCT_PRICE = '//div[@class="price-box"]/span/span/text()'

def get_prices(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            catalogue = response.content.decode('utf-8')
            parsed = html.fromstring(catalogue)

            try:
                product = parsed.xpath(XPATH_PRODUCT_NAME)
                price = parsed.xpath(XPATH_PRODUCT_PRICE)
                return [product, price]

            except IndexError:
                return

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(MEDICAMENTOS_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_catalogues = parsed.xpath(XPATH_LINKS_TO_CATALOGUES)
            #print(links_to_catalogues)

            #today = datetime.date.toxay().strftime('%d-%m-%Y')
            prices = []

            for link in links_to_catalogues:
                precios = get_prices(link)
                prices.append(precios)
            #pendiente exportar a .csv
                
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()