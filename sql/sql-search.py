import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    question = input("What action would you like to perform? "
                     "(1: AVG, 2: MAX, 3: MIN, OR 4: SUM)"
                     "\n To exit, type 5! ------- ")

    while True:
        if question == "1":
            c.execute("SELECT avg(number) FROM integers")
            rows = c.fetchone()[0]
            print('The average of all numbers is', rows)
            break
        elif question == "2":
            c.execute("SELECT DISTINCT max(number) FROM integers")
            rows = c.fetchone()[0]
            print('The maximum number is', rows)
            break
        elif question == "3":
            c.execute("SELECT DISTINCT min(number) FROM integers")
            rows = c.fetchone()[0]
            print('The minimum number is', rows)
            break
        elif question == "4":
            c.execute("SELECT sum(number) FROM integers")
            rows = c.fetchone()[0]
            print('The sum of all numbers is', rows)
            break
        elif question == "5":
            print("Thank you for playing the game. Hope to see you again!")
            break
        else:
            question = input("What action would you like to perform? "
                             "(1: AVG, 2: MAX, 3: MIN, OR 4: SUM)"
                             "\n To exit, type 5! ------- ")
