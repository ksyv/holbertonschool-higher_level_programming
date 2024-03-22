#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys


def main():
    """start of prog"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd="", db=sys.argv[3])
    state_name = sys.argv[4]
    escape_strings = ["\x00", "\n", "\r", "\\", "'", '\"', r"\xla"]
    for i in escape_strings:
        if i in state_name:
            return
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states \
                WHERE cities.state_id = states.id \
                AND states.name= '{}' \
                ORDER BY id".format(sys.argv[4]))
    cities = cur.fetchall()
    for city in cities:
        print(city[1], end='')
        if cities.index(city) != len(cities) - 1:
            print(", ", end="")
        else:
            print()
    if not len(cities):
        print()


if __name__ == "__main__":
    main()
