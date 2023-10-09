import requests
from bs4 import BeautifulSoup

GOOGLE_FORM="https://docs.google.com/forms/d/e/1FAIpQLScoaPEC2GQ5C9SzVrEiQA4hgC-2iKSe93V1kZBO2FHAS7Cw6w/viewform?usp=sf_link"
ZILLOW_MAP="https://www.zillow.com/winnipeg-mb/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Winnipeg%2C%20MB%22%2C%22mapBounds%22%3A%7B%22west%22%3A-97.69226236914062%2C%22east%22%3A-96.61285563085937%2C%22south%22%3A49.585820215006905%2C%22north%22%3A50.12061051116347%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792442%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"

HEADERS={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Upgrade-Insecure-Requests": "1"
}

response = requests.get(url=ZILLOW_MAP, headers=HEADERS)
# print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

houses = soup.select("address[data-test='property-card-addr']")
addresses = [house.getText() for house in houses]
print(addresses, len(addresses))

houses = soup.select("span[data-test='property-card-price']")
prices=[house.getText().split("$")[1].split("/")[0].replace(",","") for house in houses]

houses = soup.select("article div div a[tabindex='0']")
links = [house["href"] for house in houses]

# print(len(addresses))
# print(len(prices))
# print(len(links))