from flask import Flask, render_template, request, redirect, jsonify, url_for
from user_operation import do_login, do_sign_up
from settings import TEMPLATE_DIR, STATIC_DIR

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            user_name = request.json['user_name']
            user_key = request.json['user_key']
            if not user_key or not user_name:
                raise Exception("User name/password is not filled")
            if do_login(user_name, user_key):
                return jsonify({'result': True})
            else:
                raise Exception("invalid user&password")
        elif request.method == 'GET':
            return render_template("index.html")
        else:
            raise Exception("invalid request type")
    except Exception as e:
        print(str(e))
        return jsonify({'result': False, 'message': str(e)})


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("success.html")


@app.route('/signup', methods=['POST'])
def signup():
    try:
        if request.method == 'POST':
            user_name = request.json.get('user_name')
            user_key = request.json.get('user_key')
            if not user_key or not user_name:
                raise Exception("User name/password is not filled")
            do_sign_up(user_name, user_key)
            return jsonify({'result': True})
        else:
            raise Exception("invalid http request")
    except Exception as e:
        print(str(e))
        return jsonify({'result': False, 'message': str(e)})
