# def shout(text):
#     return text.upper()
# def whisper(text):
#     return text.lower()

# def say(func):
#     said = func("""hello everyone my name is vedant""")

#     print(said)  

# say(shout)          

# print(shout("hello"))    

# a = shout

# print(a("hello"))

# def create_adder(x):
#     def adder(y):
#         return x*y
#     return adder 

# demo = create_adder(4)

# print(demo(4))


#

try:
    a = int(input("enter first number:   "))
    b = int(input("enter second number:   "))
    c = a/b
    print("your answer is:    " ,c)
except ValueError:
    print("your value is not acceptable")
except ZeroDivisionError:
    print("your number can't divided by zero")    

else:
    print("there are no exceptence in this code")

 

