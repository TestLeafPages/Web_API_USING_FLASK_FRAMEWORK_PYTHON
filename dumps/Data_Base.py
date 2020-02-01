import sqlite3


def get_connection():
    con = sqlite3.connect('filename')
    print('DataBase opened')


def create_table(con):
    con.execute('''CREATE TABLE IF NOT EXISTS leaf_db(
    NAME TEXT NOT NULL,
    USERNAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PASSWORD TEXT NOT NULL)''')
    print('Table created')
    con.close()


def insert_records(con, obj):
    data = " INSERT INTO leaf_db(NAME, USERNAME, EMAIL, PASSWORD) VALUES (?,?,?,?)"
    con.execute(data, (obj.name, obj.username, obj.email, obj.password))
    con.commit()
    print('Record inserted')


def update_records(con, obj):
    qr = "UPDATE leaf_db set NAME = ? where EMAIL= ? "
    con.execute(qr, (obj.name, obj.email))
    con.commit()
    print('Updated')


def fetch_records(con):
    qr = "SELECT * FROM leaf_db"
    data = con.execute(qr)
    print(data)


def close_connection(con):
    con.close()
    print('DataBase closed')
