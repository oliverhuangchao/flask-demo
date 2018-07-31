from db_action import DBActionHandler
from settings import USER_TABLE


def do_sign_up(user_name, user_key):
    try:
        db_handler = DBActionHandler()
        query = """
        INSERT INTO {} values("{}", "{}");
        """.format(USER_TABLE, user_name, user_key)
        db_handler.do_post(query)
    except Exception as e:
        raise e


def do_login(user_name, user_key):
    try:
        db_handler = DBActionHandler()
        query = """
        SELECT * from {} where login_name="{}" and password="{}";
        """.format(USER_TABLE, user_name, user_key)
        resp = db_handler.do_get_one(query)
        return True if resp else False
    except Exception as e:
        raise e