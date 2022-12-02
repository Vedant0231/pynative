income = int(input("enter your income:  "))

tax = 0

if income <= 500000:
    tax = 0
elif income > 500000:
    nontaxable = income - 10000
    tax = nontaxable*10 /100  
else:
    print("non taxable income")      

print(tax)    