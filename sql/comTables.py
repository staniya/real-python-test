import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders
    (Make TEXT, Model TEXT, Order_Date TEXT)""")

    cars = [
        ('Honda', '640d', '2017-03-05'),
        ('Honda', '640d', '2017-05-04'),
        ('Honda', '640d', '2018-01-03'),
        ('Honda', '520a', '2015-04-03'),
        ('Honda', '520a', '2012-03-03'),
        ('Honda', '520a', '2009-12-15'),
        ('Ford', '1000', '1952-01-02'),
        ('Ford', '1000', '1955-05-02'),
        ('Ford', '1000', '1980-02-02'),
        ('Ford', 'alpha', '1450-02-25'),
        ('Ford', 'alpha', '1446-05-20'),
        ('Ford', 'alpha', '1560-06-20'),
        ('Ford', 'beta', '1765-07-07'),
        ('Ford', 'beta', '1885-09-01'),
        ('Ford', 'beta', '1800-03-07')
    ]

    c.executemany("INSERT INTO order VALUES(?,?,?)", cars)

    c.execute("""
    SELECT DISTINCT inventory.Make, inventory.Model, inventory.Quantity, orders.Order_Date 
    FROM inventory, orders 
    WHERE inventory.Model = orders.Model 
    ORDER by inventory.Model 
    ASC""")

    rows = c.fetchall()

    for r in rows:
        print("Make:", r[0]),
        print("Model:", r[1]),
        print("\nQuantity", r[2]),
        print("\nOrder dates", r[3])
