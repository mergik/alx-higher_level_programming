#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1:4]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
