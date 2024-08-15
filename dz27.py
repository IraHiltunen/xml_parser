import requests
from bs4 import BeautifulSoup
from xml import etree
from lxml import etree

 # Виділити для кожної новини Заголовок, посилання на статтю та текст(якщо є)


response = requests.get("https://scipost.org/atom/publications/comp-ai")# можна зробити пошук інф з data.xml

bs = BeautifulSoup(response.text, "xml")

for entry in bs.find_all("entry"):
    if entry.find("title"):
        title = entry.find("title").text
    else:
        "No title"
    if entry.find("link"):
        link = entry.find("link")["href"]
    else:
        "No link"
    if entry.find("summary"):
        summary = entry.find("summary").text
    else:
        "No summary"

    user_data = {"title": title, "link": link, "summary": summary} # словник з даними

    print(user_data)

# for one_item in bs.find_all("content"): # з прикладу
#     title = one_item.find("title").text
#     #link = one_item.find("link").text
#     link = one_item.find("link")["href"]
#     info = one_item.find("summary").text
#     user_data = {"title":title, "link": link, "summary": info}
#     print(user_data)


