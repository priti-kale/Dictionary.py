# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

a={0: 10, 1: 20}
key=int(input("enter:"))
value=int(input("enter:"))
a.update({key:value})
print(a)