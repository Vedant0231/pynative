word = input("enter the word : ")

sum = len(word)
# we can take 1 if we want even because by taking 1 we skip first value 
# we can take 0 if we want odd because by taking 0 we start from  first value which is odd 
for i in range(1,sum,2):
    print(word[i])
