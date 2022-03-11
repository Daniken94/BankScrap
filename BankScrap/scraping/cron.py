
import requests
from bs4 import BeautifulSoup

import sqlite3


def my_scheduled_job():
    print("Searching in bankier.pl...")

# Connecting to bankier.pl by BeautifulSoup

    page = requests.get("http://www.bankier.pl/gielda/notowania/akcje")
    soup = BeautifulSoup(page.content, "html.parser")
    arr_all = soup.find_all('td', class_="colWalor textNowrap")
    arr_rate = soup.find_all('td', class_="colKurs")
    arr_time = soup.find_all('td', class_="colAktualizacja")
    rows = soup.find_all('tr')

# Taking titles

    titles = []
    for i in rows:
        raw_titles = i.find("a")
        if raw_titles:
            raw_titles_all = raw_titles.get("title")
            titles.append(raw_titles_all)

# Taking walor code

    u = 0
    k_walor = []
    for i in arr_all:
        raw_k_walor = soup.find_all("td", class_="colWalor textNowrap")[u].get_text()
        k_walor.append(str.strip(raw_k_walor))
        u = u+1

# Taking rate

    f = 0
    rate = []
    for i in arr_rate:
        raw_kurs = soup.find_all("td", class_="colKurs")[f].get_text()
        rate.append(str.strip(raw_kurs))
        f = f+1

# Taking datatime

    t = 0
    time = []
    for i in arr_time:
        raw_time = i.get("data-sort-value")
        time.append(raw_time)
        t = t+1

# Mixing all tables after scraping. Without mixing can't add this to database. 

    name_walor = titles[1:]
    scrap_result = []
    j=0
    for i in range(len(name_walor)):
        df3 = [name_walor[j], k_walor[j], rate[j], time[j]]
        scrap_result.append(df3)
        j = j+1

# Making connect to database and create cursor

    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    print("Connected to SQLite")


    cur.execute("""SELECT * FROM scraping_stats""")
    results = cur.fetchall()
    print("Searching in Database....")

# Searching in database. If database is empty function insert new data from scraping. 
# Else function update database by deleting outdated records and inser new ones.

    if len(results) < 1:
        print("I need more data")
        sql = """INSERT INTO scraping_stats(name, code, price, date) VALUES(?,?,?,?)"""
        cur.executemany(sql, scrap_result)
        conn.commit()
        print("Complete!!!")
    else:
        print("I think I have outdated data")
        cur.execute("DELETE FROM scraping_stats;")
        print('You have deleted', cur.rowcount, 'outdated records from the table.')
        conn.commit()
        sql = """INSERT INTO scraping_stats(name, code, price, date) VALUES(?,?,?,?)"""
        cur.executemany(sql, scrap_result)
        conn.commit()
        print("Complete!!!")

# close connect to database

    conn.close()

my_scheduled_job()