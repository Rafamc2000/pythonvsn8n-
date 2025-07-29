import requests
from bs4 import BeautifulSoup

#URL DO SCRAPING

url = "https://www.mercadolivre.com.br/console-nintendo-switch-11-32gb-mario-kart-8-deluxe/p/MLB27870141#polycard_client=search-nordic&searchVariation=MLB27870141&wid=MLB3934653575&position=7&search_layout=grid&type=product&tracking_id=cfcd6b2a-7614-4f60-9f3e-16de96ea3659&sid=search"
header = {
    "User=Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=header) 
soup = BeautifulSoup(response.text, "html.parser")

print(soup.select_one("span.andes-money-amount "))