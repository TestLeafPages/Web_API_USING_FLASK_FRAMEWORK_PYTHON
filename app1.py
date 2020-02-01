from flask import Flask, render_template, request
from Data_Base import DataBaseFile
from TestData import TestData

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def login_page():
    return render_template("loginpage.html")


@app.route('/register', methods=["GET", "POST"])
def register_page():

    if request.method == 'POST':
        name = request.form.get("NAME")
        username = request.form.get("UNAME")
        email = request.form.get("EMAIL")
        password = str(request.form.get("PASSWORD"))
        print(name, username, email, password)

        new_record = TestData(name=name, username=username, email=email, password=password)
        con = create_object.get_connection()
        create_object.create_table(con, "table_name")
        create_object.insert_records(con, new_record)
        create_object.close_connection(con)
    return render_template("register.html")


@app.route('/reg')
def register_sample():
    return render_template("RegisterSample.html")


if __name__ == "__main__":
    create_object = DataBaseFile("leaf_taps.db")
    app.run(debug=True, port=5001)
