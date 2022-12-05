num = input("enter the list:  ").split()

first_number = num[0]
last_number = num[-1]


if first_number == last_number:
    print("accept")
else:
    print("not accept")    



password = input("enter your password:  ")

if password == "password123":
    print("your password is correct")
else:
    print("your password is not correct")    