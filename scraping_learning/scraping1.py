import requests 
from bs4 import BeautifulSoup

r = requests.get("https://www.linkedin.com/feed/")


soup = BeautifulSoup(r.content, "lxml")

soup.find("li",attrs = {"class" : "language-selector__item"})

items = soup.find_all("li",attrs = {"class" : "language-selector__item"})

for item in items: 
    print(item.button.text)

