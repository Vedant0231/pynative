def add_func(number):
    def sub_add(number):
        return number+1
    result = sub_add(number)
    return result  

print(add_func(4))

def loud(text):
    return text.upper()

def low(text):
    return text.lower()    

def greet(func):
    demo = func('''Exercises will help you to understand the topic deeply. Exercise for each tutorial topic so you can practice and improve your Python skills.''')    
    print(demo)

greet(loud) 
greet(low)   

def hello_decorator(func):

	
	def inner1():
		print("Hello, this is before function execution")
		func()

		print("This is after function execution")
		
	return inner1

def function_to_be_used():
	print("This is inside the function !!")

function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()
