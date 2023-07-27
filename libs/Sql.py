import sys
import os
import sqlite3

class Sql():
    #
    # Initialize Sql
    #
    def __init__(self, name, timeout = 100):
        try:
            self._Sql = sqlite3.connect(
                os.path.dirname(__file__) + '/../data/' + name + '.db',
                timeout = timeout
            )
        except:
            print("Can't connect to database...")

    #
    # Rollback
    #
    def rollback(self):
        try:
            self._Sql.rollback()

        except:
            print("Can't rollback, connection error?")

    #
    # Convert Tuple to List
    #
    def convert(self, data):
        return [list(elem) for elem in data]

    #
    # Create Table
    #
    def createTable(self, table, values):
        try:
            c = self._Sql.cursor()
            self._Sql.execute('CREATE TABLE if not exists ' + table + ' (' + values + ')')
            self._Sql.commit()

            return True

        except:
            print('SQL Error:', sys.exc_info()[1])
            self.rollback()
            return False

    #
    # Execute sql query
    #
    def execute(self, query, values = [], fetch = False, commit = True):
        try:
            c = self._Sql.cursor()

            c.execute(query, values)

            if (fetch):
                result = c.fetchall()

            else:
                result = True

            if (commit):
                self._Sql.commit()

            return result

        except:
            print('SQL Error:', sys.exc_info())
            self.rollback()
            return False

    #
    # Compress a table
    #
    def compress(self):
        try:
            self._Sql.execute('VACUUM')
            self._Sql.commit()
            return True

        except:
            return False

    #
    # Commit
    #
    def commit(self):
        try:
            self._Sql.commit()
            return True

        except:
            return False

    #
    # Close Connection
    #
    def close(self):
        try:
            self._Sql.close()
            return True

        except:
            return False
