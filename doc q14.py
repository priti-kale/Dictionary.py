# Q14.Write a Python program to multiply all the items in a dictionary.
# Input: dict = {‘value1’:5, ‘value2’:4, ‘value3’:3, ‘value4’:2, ‘value5’:1}


dict1={'value1':5,'value2':4,'value3':3,'value4':4}
mul=1
for i in dict1:
    mul=mul*dict1[i]
print(mul)

