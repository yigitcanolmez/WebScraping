>import requests

>from bs4 import BeautifulSoup

>r = requests.get("https://www.linkedin.com/feed/")

>r.status_code

>r.content

>soup = BeautifulSoup(r.content, "lxml")

>soup.find("li",attrs = {"class" : "language-selector__item"})

* istenilen class a ait tek bir tane li değeri getirildi.

Amacım dil seçeneklerinde bulunan dilleri almak;
<img width="1440" alt="image" src="https://github.com/yigitcanolmez/WebScraping/assets/90285509/0cdc26a7-7e70-485b-a00c-bfba4ddf6a91">

li taginda ve language-selector__item sınıfında olduğunu farkediyorum. ardından

> items = soup.find_all("li",attrs = {"class" : "language-selector__item"}) 

> for item in item:
>       print(item.button.text)

<img width="773" alt="image" src="https://github.com/yigitcanolmez/WebScraping/assets/90285509/17f1dd01-3192-4ba8-862b-8495bd40f56a">

veriler şuan elimde
