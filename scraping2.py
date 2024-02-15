import requests
from bs4 import BeautifulSoup

r = requests.get("https://boxofficeturkiye.com/hafta-sonu/detay/2024-7/")

soup = BeautifulSoup(r.content, "lxml")

names = soup.find_all("div",attrs = {"class" : "movie-name-and-release-date"})

viewers = soup.find_all("td", attrs={"class" : "column--numeric column--revenue"})

for i in range(1,10):
    name = names[i].a.text
    view = viewers[i].span.text
    print("{} : {}".format(name,view))