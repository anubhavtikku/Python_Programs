class MyException(Exception):
    def __str__(self):
        return "Invalid Age"




if __name__=="__main__":
    i=int(input(""))
    try:
        if i<18 or i>60:
            raise MyException()
        print('Valid Age ')
        
    except Exception as ob:
        print(ob)
