f=open("C://Users//Mahe//Desktop//e1.csv","a+")
f.seek(0)
l=True
while l:
    print("1.Display records 2.Insert record 3.Search Record 4.Delete record ")

    i=int(input("Enter 1 , 2 , 3 or 4 "))
    
    if i==1:
        print(f.read)

    elif i==2:
        f.seek(0,2)
        inp=input("Enter data in format")
        inp=inp+"\n"

    elif i==3:
        r=input("Enter record no. to be searched")
        f=open("C://Users//Mahe//Desktop//e1.csv","a+")
        f.seek(0)
        while f.readline():
            st=f.readline()
            l=st.split(',')
            if l[0]==r:
                print(st)
 
