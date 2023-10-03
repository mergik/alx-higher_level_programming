#!/usr/bin/python3
"""
script that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database, user_input = argv[1:5]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' " \
            "ORDER BY id ASC".format(user_input)
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
