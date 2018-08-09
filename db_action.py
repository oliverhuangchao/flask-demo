import sqlite3
from settings import WORKING_DIR, DB_PATH, USER_TABLE
import os
ERROR_PREFIX = "[DB_ERROR]"


class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance


class DBActionHandler:
    __metaclass__ = SingletonType

    def __init__(self):
        self.db_path = os.path.join(WORKING_DIR, DB_PATH)
        print(self.db_path)
        conn = sqlite3.connect(self.db_path)
        conn.close()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS {} (login_name VARCHAR PRIMARY KEY, password VARCHAR);
        """.format(USER_TABLE)
        c.execute(query)
        conn.close()

    def do_post(self, query_str):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute(query_str)
            conn.commit()
            conn.close()
        except Exception as e:
            print("{}:{}".format(ERROR_PREFIX, str(e)))
            raise e

    def do_get_many(self, query_str):
        """
        do the get str, but for multiple records
        :param query_str:
        :return:
        """
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            resp = c.execute(query_str)
            raw_rt = resp.fetchall()
            conn.close()
            if raw_rt:
                return raw_rt
            else:
                return None
        except Exception as e:
            print("{}:{}".format(ERROR_PREFIX, str(e)))
            raise e

    def do_get_one(self, query_str):
        """
        do the get str, but for only one record
        :param query_str:
        :return:
        """
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            resp = c.execute(query_str)
            raw_rt = resp.fetchall()
            conn.close()
            if raw_rt:
                return raw_rt[0]
            else:
                return None
        except Exception as e:
            print("{}:{}".format(ERROR_PREFIX, str(e)))
            raise e
