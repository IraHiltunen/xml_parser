#from lxml import etree

import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.pravda.com.ua/rss/view_news/")# можна зробити пошук інф з data.xml

# bs = BeautifulSoup(response.text, "xml")

# print(bs.title) # покаже title

# for one_item in bs.find_all("item"):
#     title = one_item.find("title").text
#     link = one_item.find("link").text
#     pub_date = one_item.find("pubDate").text
#     user_data = {"title":title, "link": link, "pub_date": pub_date}
#     print(user_data)

# for one_item in bs.find_all("content"):
#     print(one_item)
# dom = etree.XML(str(bs.find("rss")))
# print(dom.xpath('//title'))
# for item in dom.xpath('//title'):
#     print(item)

response = requests.get("https://kredobank.com.ua/info/kursy-valyut/commercial")
bs = BeautifulSoup(response.text, "html.parser")
table_root = bs.find('div', **{"class": "table-striped table-striped_special js-table"})
c = 0
for currency_data in table_root.find_all("tr"):# пачкою парсимо, а потім вибираємо по елементах
    if c == 0:
        c += 1
        continue
    currency_info = currency_data.find_all('td')
    result = {"name": currency_info[1].text, "value1": currency_info[2].text, "value2": currency_info[3].text}
    print(result)


# for one_item in bs.find('div', **{"class": "table-striped table-striped_special js-table"}):
#     print(one_item)