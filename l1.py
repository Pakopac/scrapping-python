import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020'
page = requests.get(url)
request_text = page.text
content = BeautifulSoup(request_text, "html.parser")

print(f"{'='*100}\nContent HTML\n")
print(content.prettify())
print(f"{'='*100}\nCount Table\n")
print(len(content.findAll("table")))
print(f"{'='*100}\n2 first tables\n")
print(content.findAll("table", limit=2))
print(f"{'='*100}\nClub table\n")
clubs = content.find("table", {"class": "wikitable"})
print(clubs.prettify())
print(f"{'='*100}\nPrint clubs\n")
rows = clubs.findAll("tr", limit=20)[1:20]
array = []
for tr in rows:
    print(tr.find("a"))
    array.append({"clubs": tr.find('a').getText(), "url": tr.find('a').get('href')})
    print(f"name: {tr.find('a').getText()}")
    print(f"url: {tr.find('a').get('href')}")
    print("------")

df = pd.DataFrame(array)
df.style
print(df.head())
df.to_csv('clubs.csv', index=False)  