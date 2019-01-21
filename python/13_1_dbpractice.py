# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
import sqlite3 as dbms

con=dbms.connect('test.db')
cur=con.cursor()
cur.execute('CREATE TABLE test_date(birthday DATE, name text, group_name SMALLINT )')
cur.execute("INSERT INTO test_date values('1986-06-20', 'OJJY', 1)")
cur.execute('select * from test_date')
print(cur.fetchall())
cur.execute('Drop TABLE test_date')
con.commit()
con.close()

