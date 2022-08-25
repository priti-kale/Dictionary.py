# Q15.Write a Python program to remove a key from a dictionary.

myDict = {'a':1,'b':2,'c':3,'d':4}
a=input("enter:")
print(myDict)
if 'a' in myDict: 
    del myDict[a]
print(myDict)