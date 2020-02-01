import sqlite3
from flask import Flask, render_template, request

from Data_Base import DataBaseFile

app = Flask(__name__)

filename = 'leaf_taps.db'


def get_connection():
    con = sqlite3.connect(filename)
    print('DataBase opened')
    return con


def create_table(con):
    con.execute('''CREATE TABLE IF NOT EXISTS leaf_db(
    NAME TEXT NOT NULL,
    USERNAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PASSWORD TEXT NOT NULL)''')
    print('Table created Successfully')


def insert_records(con, obj):
    data = "INSERT INTO leaf_db(NAME, USERNAME, EMAIL, PASSWORD) VALUES (?,?,?,?)"
    con.execute(data, (obj.name, obj.uname, obj.email, obj.pwd))
    con.commit()
    print('Record inserted')

class DataRelated:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.uname = kwargs.get('uname')
        self.email = kwargs.get('email')
        self.pwd = kwargs.get('pwd')


@app.route('/')
@app.route('/index')
def login_page():
    return render_template("loginpage.html")


@app.route('/register', methods=["GET", "POST"])
def register_page():
    if request.method == 'POST':
        name = request.form.get("NAME")
        uname = request.form.get("UName")
        email = request.form.get("email")
        pwd = str(request.form.get("password"))

        new_record = DataRelated(name=name, uname=uname, email=email, pwd=pwd)

        con = get_connection()
        create_table(con)
        insert_records(con, new_record)
        con.close()
    return render_template("register.html")


@app.route('/reg')
def register_sample():
    return render_template("RegisterSample.html")


if __name__ == "Gopi":
    app.run(debug=True, port=8000)
