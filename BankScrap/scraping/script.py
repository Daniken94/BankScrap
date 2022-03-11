from django.shortcuts import render
from django.views import View

import requests
from bs4 import BeautifulSoup

import sqlite3

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()



page = requests.get("http://www.bankier.pl/gielda/notowania/akcje")
soup = BeautifulSoup(page.content, "html.parser")
arr = soup.find_all('td', class_="colWalor textNowrap")
arrkurs = soup.find_all('td', class_="colKurs")
arrczas = soup.find_all('td', class_="colAktualizacja")
rows = soup.find_all('tr')

titler = []

for titles in rows:
    nwalor = titles.find("a")
    if nwalor:
        wwalor = nwalor.get("title")
        titler.append(wwalor)


u = 0
kwalor = []
for i in arr:
    arr2 = soup.find_all("td", class_="colWalor textNowrap")[u].get_text()
    kwalor.append(str.strip(arr2))
    u = u+1


f = 0
kurs = []
for i in arrkurs:
    arr2 = soup.find_all("td", class_="colKurs")[f].get_text()
    kurs.append(str.strip(arr2))
    f = f+1


t = 0
czas = []
for i in arrczas:
    czas_prime = i.get("data-sort-value")
    czas.append(czas_prime)
    t = t+1


name = titler[1:]
new = []
j=0
for i in range(len(name)):
    df3 = [name[j], kwalor[j], kurs[j], czas[j]]
    new.append(df3)
    j = j+1


sql = """INSERT INTO scraping_stats(name, code, price, date) VALUES(?,?,?,?)"""

cur.executemany(sql, new)
conn.commit()
print("complete")


