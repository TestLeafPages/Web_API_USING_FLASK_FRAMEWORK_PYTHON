import sqlite3

# ================================================================================
con = sqlite3.connect('leaftaps.db')
print('DataBase Opened')
# ================================================================================
con.execute('''CREATE TABLE IF NOT EXISTS leaf_db(
NAME TEXT NOT NULL,
USERNAME TEXT NOT NULL,
EMAIL TEXT NOT NULL,
PASSWORD TEXT NOT NULL)''')
print('Table created')
# ================================================================================

con.execute('''INSERT INTO leaf_db(NAME, USERNAME, EMAIL, PASSWORD) 
            VALUES('Gopinath', 'J', 'gopinath.jayakumar@testleaf.com', 'testleaf')''')
con.commit()
print('Record inserted')
# ================================================================================

data = con.execute('''SELECT * FROM leaf_db''')
for i in data:
    print(i)
print('Read the Data')

# ================================================================================
con.execute(''' UPDATE leaf_db set NAME = 'Gopi' WHERE NAME='Sarath' ''')
con.commit()
print('Updated')
# ================================================================================

con.execute(''' DELETE from leaf_db WHERE NAME = 'Gopi' ''')
con.commit()
print('Deleted')
# ================================================================================

con.close()
print('DataBase closed')
