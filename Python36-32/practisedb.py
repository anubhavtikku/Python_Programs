import MySQLdb as db

conn=db.connect("127.0.0.1","root","tiger","hr")
cur=conn.cursor()

h=True

while h:
    i=int(input("Enter 1.Insert 2.Update 3.Delete 4.View all 5.Exit "))
    if i==1:
        i=int(input("Enter id "))
        j=input("Enter last name ")
        k=input("Enter email ")
        selqry="insert into dummy(employee_id,last_name,email,hire_date,job_id) values(%s,%s,%s,'1989-09-21 00:00:00','World')" 
        cur.execute(selqry,(i,j,k ))
        
    elif i==2:
        i=int(input("Enter id "))
        j=input("Enter first name ")
        selqry="update dummy set first_name=%s where employee_id=(%s)"
        cur.execute(selqry,(j,i))

    elif i==3:
        i=int(input("Enter id "))
        selqry="delete from dummy where employee_id=(%s)"
        cur.execute(selqry,(i,))

    elif i==4:
        selqry="select * from dummy"
        cur.execute(selqry)
        rs=cur.fetchall()
        for row in rs:
            print(row[0],row[1],row[4])

    elif i==5:
        h=False
