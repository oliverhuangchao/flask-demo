from flask import Flask, render_template, request, redirect
from db_action import DBActionHandler
from settings import USER_TABLE, TEMPLATE_DIR, STATIC_DIR

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


def init():
    """
    do init function
    :return:
    """
    DBActionHandler()


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            user_name = request.json['user_name']
            user_key = request.json['user_key']
            if not user_key or not user_name:
                raise Exception("User name/password is not filled")
            if do_login(user_name, user_key):
                return render_template("success.html")
            else:
                raise Exception("invalid user&password")
        elif request.method == 'GET':
            return render_template("index.html")
        else:
            raise Exception("invalid request type")
    except Exception as e:
        print(str(e))
        return render_template("error.html")


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
        INSERT INTO {} values("{}", "{}");
        """.format(USER_TABLE, user_name, user_key)
        db_handler.do_post(query)
    except Exception as e:
        raise e


init()
