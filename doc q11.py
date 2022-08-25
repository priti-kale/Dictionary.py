# Q11.Write a Python script to merge two Python dictionaries


a=int(input("enter the lenth:"))
k={}
for i  in range (1,a+1):
    key_name=input("enter the key:")
    key_value=input("enter the value:")
    k.update({key_name:key_value})
print(k)


