num = input("enter the list:  ").split()

first_number = num[0]
last_number = num[-1]


if first_number == last_number:
    print("accept")
else:
    print("not accept")    