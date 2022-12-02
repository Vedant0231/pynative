list1 = [1,2,4,6,5]
list2 = [2,3,1,5,6]
final_list = []

for i in list1:
    if i%2 != 0:
        final_list.append(i)

for i in list2:
    if i%2 == 0:
        final_list.append(i)

print(final_list)
