#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys


def main():
    """start of prog"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    state_name = sys.argv[4]
    escape_strings = ["\x00", "\n", "\r", "\\", "'", '\"', r"\xla"]
    for i in escape_strings:
        if i in state_name:
            return
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name= '{}' \
                ORDER BY id".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)


if __name__ == "__main__":
    main()
