import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.flipkart.com/poco-m3-cool-blue-64-gb/p/itmc8ec867cb0472?pid=MOBFZTCUDDCTDN3G&lid=LSTMOBFZTCUDDCTDN3GJBLKQ8&marketplace=FLIPKART&q=mobile&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=e9d79321-6c7b-4428-88d4-54395287a867.MOBFZTCUDDCTDN3G.SEARCH&ppt=sp&ppn=sp&ssid=4phc1a1e0w0000001633700598119&qH=532c28d5412dd75b'


def get_link_data(url):
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

print(get_link_data(url))