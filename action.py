import sqlite3
import sys
import printdb


def main():
    dbcon = sqlite3.connect('moncafe.db')
    with dbcon:
        cursor = dbcon.cursor()
        with open(sys.argv[1]) as actions:

            for line in actions:
                expression = line.split(',')
                product_id = int(expression[0])
                quantity = int(expression[1])
                activator_id = int(expression[2])
                date = int(expression[3])
                cursor.execute("SELECT quantity FROM Products WHERE id =(?)", (product_id,))
                quantity_exist = cursor.fetchone()[0]
                quantity_exist = quantity_exist + quantity

                if quantity_exist >= 0:
                    cursor.execute("UPDATE Products Set quantity =(?) WHERE id =(?)", (quantity_exist, product_id))

                    cursor.execute("INSERT INTO Activities VALUES(?,?,?,?)",
                                   (product_id, quantity, activator_id, date,))

            dbcon.commit()


if __name__ == "__main__":
    main()
    printdb.main()
