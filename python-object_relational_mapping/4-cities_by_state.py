#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys


def main():
    """start of prog"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd="", db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states \
                WHERE cities.state_id = states.id \
                ORDER BY id")
    cities = cur.fetchall()
    for citie in cities:
        print(citie)


if __name__ == "__main__":
    main()
