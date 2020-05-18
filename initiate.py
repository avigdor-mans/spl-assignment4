import sqlite3
import os
import sys
import printdb

def main():
    if os.path.exists("moncafe.db"):
        os.remove("moncafe.db")
        database = os.path.isfile('moncafe.db')

    dbcon = sqlite3.connect('moncafe.db')

    with dbcon:
        cursor = dbcon.cursor()
        cursor.execute(
            "CREATE TABLE Employees(id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary REAL NOT NULL, coffee_stand INTEGER REFERENCES Coffee_stands(id))")

        cursor.execute("CREATE TABLE Suppliers(id INTEGER PRIMARY KEY, name TEXT NOT NULL,contact_information TEXT)")

        cursor.execute(
            "CREATE TABLE Products(id INTEGER PRIMARY KEY, description TEXT NOT NULL, price REAL NOT NULL,quantity INTEGER NOT NULL)")

        cursor.execute(
            "CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY, location TEXT NOT NULL, number_of_employees INTEGER)")

        cursor.execute(
            "CREATE TABLE Activities(product_id INTEGER INTEGER REFERENCES Product(id),quantity INTEGER NOT NULL, activator_id INTEGER NOT NULL , date DATE NOT NULL)")

        with open(sys.argv[1]) as inputfile:
            for line in inputfile:
                expression = line.split(', ')
                if expression[0] == "P":
                    cursor.execute("INSERT INTO Products VALUES(?,?,?,?)",
                                   (expression[1], expression[2], expression[3], 0))

                if expression[0] == "C":
                    cursor.execute("INSERT INTO Coffee_stands VALUES(?,?,?)",
                                   (expression[1], expression[2], expression[3]))

                if expression[0] == "S":
                    cursor.execute("INSERT INTO Suppliers VALUES(?,?,?)", (expression[1], expression[2], expression[3][0:len(
                        expression[3])-1]))

                if expression[0] == "E":
                    cursor.execute("INSERT INTO Employees VALUES(?,?,?,?)", (expression[1], expression[2], expression[3], expression[4]))

    dbcon.commit()


if __name__ == "__main__":
    main()
