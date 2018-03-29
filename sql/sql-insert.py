import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE if exists integers")
    c.execute("CREATE TABLE integers(number INT)")
    for i in range(100):
        c.execute("INSERT INTO integers VALUES(?)", (random.randint(0, 100), ))
    rows = c.fetchall()
    for r in rows:
        print(r)
