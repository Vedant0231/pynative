class information:
    def __init__(self,name,age,location,std):
        self.name=name
        self.age=age
        self.location=location
        self.std=std

    def studentinfo(self):
        print("student name is: ",self.name)
        print("student age is: ",self.age)
        print("student location is: ",self.location)
        print("student std is: ",self.std)  

    def __del__(self):
        pass
        

stu2 = information("vedant","19","surat","12")   
stu2.studentinfo()

del stu2
stu2.studentinfo()
