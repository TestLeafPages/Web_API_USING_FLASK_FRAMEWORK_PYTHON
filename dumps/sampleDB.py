import sqlite3

class TestData:

    def __init__(self, **kwargs):
        self.name = kwargs['NAME']
        self.username = kwargs['USERNAME']
        self.email = kwargs['EMAIL']
        self.password = kwargs['password']


con = sqlite3.connect("sample.db")


con.execute('''CREATE TABLE IF NOT EXISTS leaf_db(
    NAME TEXT NOT NULL,
    USERNAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PASSWORD TEXT NOT NULL)''')
print('Table created')

data = "INSERT INTO leaf_db(NAME, USERNAME, EMAIL, PASSWORD) VALUES (?,?,?,?)"
obj = TestData()
con.execute(data, )