num = int(input("enter the number"))
for i in range(0,num):
    current_number = i
    if current_number >0:
        previous_number = current_number - 1
    else:
        previous_number = 0
    sum = current_number + previous_number     

    print("current number",current_number,"previous number",previous_number,'sum',sum) 
    