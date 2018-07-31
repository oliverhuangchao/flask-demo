from flask import Flask, render_template, request, redirect
from db_action import DBActionHandler
from settings import USER_TABLE
import uuid

app = Flask(__name__)


def init():
    """
    do init function
    :return:
    """
    DBActionHandler()


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            user_name = request.json.get('user_name')
            user_key = request.json.get('user_key')
            # if not user_key or not user_name:
            #     raise Exception("User name/password is not filled")
            # do_login(user_name, user_key)
            return render_template("success.html")
            # return redirect("/error")
        elif request.method == 'GET':
            return render_template("index.html")
    except Exception as e:
        print(str(e))
        return render_template("error.html", err_msg=str(e))


def do_login(user_name, user_key):
    try:
        db_handler = DBActionHandler()
        query = """
        SELECT id from {} where login_name="{}" and password="{}";
        """.format(USER_TABLE, uuid.uuid4(), user_name, user_key)
        db_handler.do_get_one(query)
    except Exception as e:
        raise e


@app.route('/signup', methods=['POST'])
def signup():
    try:
        if request.method == 'POST':
            user_name = request.json.get('user_name')
            user_key = request.json.get('user_key')
            if not user_key or not user_name:
                raise Exception("User name/password is not filled")
            do_sign_up(user_name, user_key)
            return render_template("success.html")
        else:
            raise Exception("invalid http request")
    except Exception as e:
        print(str(e))
        return render_template("error.html", err_msg=str(e))


def do_sign_up(user_name, user_key):
    try:
        db_handler = DBActionHandler()
        query = """
        INSERT INTO {} values("{}", "{}", "{}");
        """.format(USER_TABLE, uuid.uuid4(), user_name, user_key)
        db_handler.do_post(query)
    except Exception as e:
        raise e


init()
