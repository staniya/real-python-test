# INSERT Command


# import the sqlite3 library
import sqlite3

# create connection object
with sqlite3.connect("new.db") as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # insert the multiple records using a tuple
    cities = [
        ('Boston', 'MA', 600000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000)
    ]

    # insert data into table
    c.executemany('INSERT INTO population VALUES(?,?,?)', cities)
    # # insert data
    # c.execute("INSERT INTO population "
    #           "VALUES('New York City', 'NY', 8400000)")
    # c.execute("INSERT INTO population "
    #           "VALUES('San Francisco', 'CA', 800000)")

# You need the following if it wasn't a with statement
# commit the changes
#   conn.commit()
# close the database connection
#   conn.close()
