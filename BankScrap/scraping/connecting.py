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

sql = """INSERT INTO scraping_stats(name, code, price, date) VALUES(?,?,?,?)"""

cur.executemany(sql, new)
conn.commit()
print("complete")

# def data_entry():
#     for item in id:
#         cur.execute("INSERT INTO scraping_stats VALUES(?,?,?,?,?)", item)


# one = [1, 2, 3, 4]
# two = ["one", "two", "three", "four"]
# three = ["ja", "to", "jakoś", "pochytom"]

# df4 = one[3], two[3], three[3]
# print(df4)




# cur.execute('''INSERT INTO scraping_stats VALUES(?,?,?,?,?)''',(id, name, code, price, date))
# conn.commit()


cur.execute('''SELECT * FROM scraping_stats''')
results = cur.fetchall()

print(results)

# table_rows = [id, name, code, price, date]
# sql = '''INSERT INTO scraping_stats VALUES(?,?,?,?,?) '''

# cur.executemany(sql, table_rows)

# for row in cur.execute('SELECT * FROM scraping_stats'):
#     print(row)
