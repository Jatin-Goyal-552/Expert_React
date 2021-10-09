import requests
import lxml
from bs4 import BeautifulSoup

def get_link_data_amazon(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    final_price=""
    for p in price:
        if p!=",":
            final_price = final_price+p
    print(final_price)
    price = float(final_price[1:])

    return name, price

def get_link_data_flipkart(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector=".B_NuCI").getText()
    name = name.strip()
    price=""
    price = soup.select_one(selector="._30jeq3").getText()
    final_price=""
    for p in price:
        if p!=",":
            final_price = final_price+p
    # print(final_price)
    price = float(final_price[1:])

    return name, price