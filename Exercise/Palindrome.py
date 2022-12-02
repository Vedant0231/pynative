number = int(input("enter your number"))

original_number = number

reverse_number = 0

while number>0:
    reminder = number%10
    reverse_number= (reverse_number*10)+reminder
    number = number // 10

if original_number == reverse_number:
    print("this is palindrome")
else:
    print("this is not palindrome")    