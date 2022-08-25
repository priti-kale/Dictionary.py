# Write a Python program to check whether a given key already exists in a dictionary.


n=int(input("enter:"))
key=input("enter:")
i=0
dic={}
while i<n:
    key_name=input("enter key:")
    value=eval(input("enter value:"))
    dic.update({key_name:value})
    i=i+1
print(dic)
if key in dic:
    print("exists")
else:
    print("not exists")
