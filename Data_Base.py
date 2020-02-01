import sqlite3


class DataBaseFile:

    def __init__(self, filename):
        self.filename = filename

    def get_connection(self):
        con = sqlite3.connect(self.filename)
        print('DataBase opened')
        return con

    def create_table(self, con, table_name, *headers):
        con.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name + '''(
        NAME TEXT NOT NULL,
        USERNAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        PASSWORD TEXT NOT NULL)''')
        print('Table created')

    def insert_records(self, con, obj):
        data = "INSERT INTO table_name(NAME, USERNAME, EMAIL, PASSWORD) VALUES (?,?,?,?)"
        con.execute(data, (obj.name, obj.username, obj.email, obj.password))
        con.commit()
        print('Record inserted')

    def update_records(self, con, obj):
        qr = "UPDATE leaf_db set NAME = ? where EMAIL= ? "
        con.execute(qr, (obj.name, obj.email))
        con.commit()
        print('Updated')

    def fetch_records(self, con):
        qr = "SELECT * FROM leaf_db"
        data = con.execute(qr)
        print(data)

    def close_connection(self, con):
        print('DataBase Closed')
        con.close()


# class TestData:
#
#     def __init__(self, **kwargs):
#         self.name = kwargs["name"]
#         self.username = kwargs["username"]
#         self.email = kwargs["email"]
#         self.password = kwargs["password"]


# if __name__ == "__main__":
#     x = DataBaseFile('Hello.db')
#     con = x.get_connection()
#     x.create_table(con, "table1")
#     data = TestData(name="gopinath", username='Gopi', email='gopi@gmail.com', password='123')
#     x.insert_records(con, data)
#     x.close_connection(con)
