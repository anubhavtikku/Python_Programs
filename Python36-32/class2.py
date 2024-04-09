class electricity:
    f1=0.4
    f2=0.6
    f3=0.7
    c=50
    r=1.15
    def setdata(self,name,units):
        self.n=name
        self.u=units

    def getdata(self):
        if self.u<=100:
            self.c=self.c+self.f1*self.u

        elif self.u>100 and self.u<=300:
            self.c=self.c+self.f1*100+self.f2*(self.u-100)

        else:
            self.c=self.c+self.f1*100+self.f2*200+self.f3*(self.u-300)

        print(self.n,self.c)
    
name=input("Enter name ")
units=int(input("Enter electricity units used "))
ob=electricity()
ob.setdata(name,units)
ob.getdata()
