def add_func(number):
    def sub_add(number):
        return number+1
    result = sub_add(number)
    return result  

print(add_func(4))

