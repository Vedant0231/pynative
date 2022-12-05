# numbers = []

# for i in range(0, 5):
#     print("Enter number at location", i, ":")
#     item = float(input())
#     numbers.append(item)

# print("User List:", numbers)

number1= float(input("enter the value:  "))
number2 = float(input("enter second number: "))

opration= input("enter your opration")

if opration =="+":
    print( number1+number2)
elif opration =="-":
    print( number1-number2)
elif opration =="%":
    print(number1%number2)
elif opration =="*":
    print(number1*number2)            
else:
    print("opration is not valide")    