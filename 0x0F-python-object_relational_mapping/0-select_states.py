#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1:4]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
