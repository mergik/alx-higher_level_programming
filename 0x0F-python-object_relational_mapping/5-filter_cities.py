#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database, state_name = argv[1:5]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )
    query = "SELECT cities.name\
            FROM cities JOIN states\
            ON cities.state_id = states.id WHERE states.name = %s"
    cursor = db.cursor()
    cursor.execute(query, (state_name, ))
    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    db.close()
