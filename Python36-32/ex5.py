n1=input("Write something ")
if len(n1)<3:
    print(n1)
else:
    if n1[len(n1)-3:]=="ing":
        n1=n1+"ly"
        print(n1)
    else:
        n1=n1+"ing"
        print(n1)
       
    
