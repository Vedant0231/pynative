person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
print(person.get("name"))
print(person["name"])
print(person.keys())
print(person.values())
print(person.items())

person["name"]="vedant"

print(person)

person={"name":"vedant","age":22,"location":"surat"}

print(person)

person["name"]="deep"
print(person)

dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}

dict1.update(dict2)
print(dict1)

student_dict1 = {'Aadya': 1, 'Arul': 2, }
student_dict2 = {'Harry': 5, 'Olivia': 6}
student_dict3 = {'Nancy': 7, 'Perry': 9}

student_dict = {**student_dict1, **student_dict2, **student_dict3}
print(student_dict)

telephone_book = [1178, 4020, 5786]
persons = ['Jessa', 'Emma', 'Kelly']

telephone_Directory = {key: value for key, value in zip(persons, telephone_book)}
print(telephone_Directory)


dict = {1:'aaa',2:'bbb',3:'AAA'}
print('Maximum Key',max(dict))
print('Minimum Key',min(dict)) 