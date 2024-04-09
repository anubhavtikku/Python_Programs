import MySQLdb as db

conn=db.connect("127.0.0.1","root","tiger","hr")
cur=conn.cursor()

h=True

while h:
    
    i=input("Enter username ")
    j=input("Enter password ")
    k=0
    selqry="select * from login"
    cur.execute(selqry)
    rs=cur.fetchall()
    for row in rs:
        if row[0]==i and row[1]==j:
            k=1

    if k==1:
        selqry="select * from det where id="+i
        cur.execute(selqry)
        rs=cur.fetchall()
        for row in rs:
            print(row[1])
        break;
    else:
        print("Wrong Details")
        
    
