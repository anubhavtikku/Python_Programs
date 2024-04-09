import sqlite3 as sq

#conn=sq.connect(":memory:")
conn=sq.connect("employeesdb")
cur=conn.cursor()
qy="create table if not exists employees(eid int,name text,address text)"
cur.execute(qy)

qryinsert="delete from employees"
cur.execute(qryinsert)

eid=input("Enter employee id :")
ename=input("Enter name:")
address=input("Enter address:")

qryinsert="insert into employees values(?,?,?)"
cur.execute(qryinsert,(eid,ename,address))

qryinsert="insert into employees values(101,'James','Noida')"
cur.execute(qryinsert)
conn.commit()

qryselect="select * from employees"
cur.execute(qryselect)
rs=cur.fetchall()
for row in rs:
    print("{0[0]} {0[1]} {0[2]}".format(row))
    
print("\n\n")
i=input("Enter employee id :")


qrydel="delete from employees where eid=?"
cur.execute(qrydel,(i,))

conn.commit()
print("connection is stable")
qryselect="select * from employees"
cur.execute(qryselect)
rs=cur.fetchall()
for row in rs:
    print("{0[0]} {0[1]} {0[2]}".format(row))
cur.close()
conn.close()
