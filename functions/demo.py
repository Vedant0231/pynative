# demo = eval(input("enter your opration:   "))
# print(demo)

# a = int(input("enter your number:   "))
# b=[1,2,3,4,5,6,7,8]

# if a in b:
#     print("present")
# else:
#     print("not present")    

def is_even(list1):
    even_num = []
    for n in list1:
        if n % 2 == 0:
            even_num.append(n)
    # return a list
    return even_num

# Pass list to the function
even_num = is_even([3,5,1,7,9,2])
print("Even numbers are:", even_num)