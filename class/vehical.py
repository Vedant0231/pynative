# this is a example of inheritance in oops. We can use function from common class in vehicals class by inheritance.

class common:
    def commonfunction(self): 
        print("this are used for traveling")

class vehicals(common):
    def __init__(self, name, color, price, year):
        self.name=name
        self.color=color
        self.price=price
        self.year=year
    
    def bike(self):
        print("bike name is:  " ,self.name)
        print("bike color is: " ,self.color)
        print("bike price is: " ,self.price)
        print("bike year  is: " ,self.year)

    def car(self):
        print("car name is:  " ,self.name)
        print("car color is: " ,self.color)
        print("car price is: " ,self.price)
        print("car year  is: " ,self.year)

vehical1 = vehicals("hunter360","red","200000","2022")
vehical1.bike()
vehical1.commonfunction()
print(vehical1)

vehical2 = vehicals("swift","black","800000","2020")
vehical2.car()
print(vehical2)
<<<<<<< HEAD

=======
>>>>>>> ae314414c47f8776e9fd3aa3bccb780b896beb17
