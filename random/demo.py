import random
num1=int(input("enter your number: "))
num2 = random.randint(0,9)

if num1 == num2:
    print("your are correct")
else:
    print("not correct")   

print(num2)     