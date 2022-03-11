import sqlite3

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()


name = ["spółka akcyjna", "spółka nieakcyjna"]
code = ["TWKJYO", "KJGTOS"]
price = ["1234,234", "54,987"]
date = ["2022-03-11 09:20", "2022-03-11 09:20"]

new = []
j=0
for i in range(len(name)):
    df3 = [name[j], code[j], price[j], date[j]]
    new.append(df3)
    j = j+1

# sql = """INSERT INTO scraping_stats(name, code, price, date) VALUES(?,?,?,?)"""

# cur.executemany(sql, new)
# conn.commit()
# print("complete")

cur.execute("DELETE FROM scraping_stats;")
print('We have deleted', cur.rowcount, 'records from the table.')
conn.commit()









cur.execute('''SELECT * FROM scraping_stats''')
results = cur.fetchall()

print(results)

conn.close()