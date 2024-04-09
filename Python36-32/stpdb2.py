import MySQLdb as db

conn=db.connect("127.0.0.1","root","tiger","hr")
selqry="select * from employees"
cur=conn.cursor()
cur.execute(selqry)
rs=cur.fetchall()
for row in rs:
    print(row[0],row[1])
