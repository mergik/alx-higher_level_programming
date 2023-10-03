#!/usr/bin/python3
"""
script that takes in arguments
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, but now safe from MySQL injections
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database, user_input = argv[1:5]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor = db.cursor()
    cursor.execute(query, (user_input, ))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
