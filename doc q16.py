# Q15.Write a Python program to remove a key from a dictionary.


mydict = {'a':1,'b':2,'c':3,'d':4}
a=input("enter:")
for i in mydict:
    if i==a:
        mydict.remove({i:a[i]}) 
        print(a[i])
print(mydict)