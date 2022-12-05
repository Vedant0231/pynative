#update value in class
class student:
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def info(self):
        print("student name is: ",self.name)
        print("student age is: ",self.age)
        print("student std is: ",self.std)
        
    def updateprof(self,student_age,student_std):
        self.age=student_age
        self.std=student_std

student1 = student("vedant","18","11th")

student1.info()

student1.updateprof("19","12th")

student1.info()
