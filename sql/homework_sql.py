import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    car = [
        ('Honda', '640d', 120),
        ('Honda', '520a', 200),
        ('Ford', '1000', 30),
        ('Ford', 'alpha', 40),
        ('Ford', 'beta', 50)
    ]
    c.executemany("INSERT INTO inventory VALUES(?,?,?)", car)

    c.execute("UPDATE inventory SET Quantity=400 "
              "WHERE Make='Honda'")

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * from inventory WHERE make='Ford'")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output headers
    print('Make Model Qty')
    print('--------------')

    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1], r[2])


