import sqlite3
import os
import sys


def main():
    dbcon = sqlite3.connect('moncafe.db')
    with dbcon:
        cursorTableData = dbcon.cursor()
        cursor2 = dbcon.cursor()
        cursorTableData.execute("SELECT * FROM Activities ORDER BY date ASC")
        print("Activities")
        lines = cursorTableData.fetchall()
        for line in lines:
            print(line)

        cursorTableData.execute("SELECT * FROM Coffee_stands ORDER BY id ASC")
        print("Coffee stands")
        lines = cursorTableData.fetchall()
        for line in lines:
            print(line)

        cursorTableData.execute("SELECT * FROM Employees ORDER BY id ASC")
        print("Employees")
        lines = cursorTableData.fetchall()
        for line in lines:
            print(line)

        cursorTableData.execute("SELECT * FROM Products ORDER BY id ASC")
        print("Products")
        lines = cursorTableData.fetchall()
        for line in lines:
            print(line)

        cursorTableData.execute("SELECT * FROM Suppliers ORDER BY id ASC")
        print("Suppliers")
        lines = cursorTableData.fetchall()
        for line in lines:
            print(line)

        cursorTableData.execute("SELECT * FROM Activities")
        num = len(cursorTableData.fetchall())

        if num > 0:
            print("")
            print("Employees report")
            cursorTableData.execute(
                "SELECT Employees.id, name, salary, location FROM Employees JOIN Coffee_stands ON "
                "Employees.coffee_stand = Coffee_stands.id ORDER BY Employees.name ASC")
            employee = cursorTableData.fetchall()
            for line in employee:
                cursor2.execute("SELECT Activities.quantity, Activities.Product_id, Products.price FROM Activities "
                                "JOIN Products ON Activities.Product_id = Products.id WHERE Activities.quantity < 0 "
                                "AND Activities.activator_id = (?)", (line[0],))
                sales = cursor2.fetchall()
                total = 0
                for line2 in sales:
                    total = total + (-line2[0]) * line2[2]
                print(str(line[1]) + " " + str(line[2]) + " " + str(line[3]) + " " + str(total))
            print("")
            print("Activities")
            cursorTableData.execute("SELECT Activities.date, Products.description, Activities.quantity, "
                                    "Employees.name, "
                                    "Suppliers.name FROM Activities JOIN Products ON Activities.product_id = "
                                    "Products.id LEFT JOIN Employees ON Activities.activator_id = "
                                    "Employees.id LEFT JOIN Suppliers ON Activities.activator_id = Suppliers.id ORDER BY date ASC")
            activities = cursorTableData.fetchall()
            for line in activities:
                print(line)


if __name__ == "__main__":
    main()
