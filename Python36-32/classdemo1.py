class employee:
    def setdata(self,iid,name):
        self.__sid=iid
        self.__name=name

    def getdata(self):
        print("id={} name={} ".format(self.__sid,self.__name))

ob=employee()
ob.setdata(1,"abc")
ob.getdata()

employee().setdata(2,"b")

