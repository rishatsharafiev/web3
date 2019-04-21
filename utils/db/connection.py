from sqlite3 import connect, Error

from settings import DATABASE_PATH


def get_connection():
    try:
        return connect(DATABASE_PATH)
    except Error as e:
        print("Error:{}".format(e.args[0]))
        raise e
