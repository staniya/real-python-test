import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("SELECT * FROM inventory")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        # output the car make, model and quantity to the screen
        print(r[0] + r[1])
        print(r[2])

        # retrieve order_data f or the current car make and model
        c.execute("SELECT count(Order_Date) FROM orders WHERE make=? and model=?",
                  (r[0], r[1]))

        # fetchone() retrieves one record from the query
        order_count = c.fetchone()[0]

        # output the order count to the screen
        print(order_count)
        print("\n")

    # sql = {
    #     '640d count': "SELECT count(Make) FROM orders WHERE Model='640d'",
    #     '520a count': "SELECT count(Make) FROM orders WHERE Model='520a'",
    #     '1000 count': "SELECT count(Make) FROM orders WHERE Model='1000'",
    #     'alpha count': "SELECT count(Make) FROM orders WHERE Model='alpha'",
    #     'beta count': "SELECT count(Make) FROM orders WHERE Model='beta'"
    # }
    #     # print(keys.replace(" '", "") + ':', r[0])
    #
    # select_sql = {'640d quantity': "SELECT quantity "
    #                                "FROM inventory WHERE Model='640d'",
    #               '520a quantity': "SELECT quantity "
    #                                "FROM inventory WHERE Model='520a'",
    #               '1000 quantity': "SELECT quantity "
    #                                "FROM inventory WHERE Model='1000'",
    #               'alpha quantity': "SELECT quantity "
    #                                "FROM inventory WHERE Model='alpha'",
    #               'beta quantity': "SELECT quantity "
    #                                 "FROM inventory WHERE Model='beta'"
    #               }
    # for keys, values in sql.items():
    #     c.execute(values)
    #     rate = c.fetchone()
    #     for keys2, values2 in select_sql.items():
    #         c.execute(values2)
    #         c.execute("SELECT Make, Model FROM inventory")
    #         r = c.fetchone()
    #         print(r[0] + r[1])
    #         print(keys2 + ":", r[0])
    #         print(keys + ":", rate[0])
    #         print("---------------------------")
