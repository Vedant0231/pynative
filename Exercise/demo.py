list1= input("enter your list:   ").split()
demo_list=[]

for num in list1:
    if int(num)%2==0:
        demo_list.append(num)
    else:
        demo_list.append("*")
print(demo_list)        

