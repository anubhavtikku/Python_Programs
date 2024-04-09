class student:
    def getdata(self,n,a):
        self.name=n
        self.age=a
        
    def setdata(self):
        print(self.name)
        print(self.age)

ob=student()
name=input("Enter name ")
age=input("Enter age ")
ob.setdata(name,age)
ob.getdata()
#student().setdata("Hello",0)
#student().getdata()
