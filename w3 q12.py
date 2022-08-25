# 12. Write a Python program to remove a key from a dictionary.
# a={'padhmavti':87,'rajesh':98,'riya':54}

myDict = {'a':1,'b':2,'c':3,'d':4}
if 'a' in myDict: 
	del myDict['a']
print(myDict)