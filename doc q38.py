# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

a={'c1': 'Red', 'c2': 'Green', 'c3': None}
d={}
for i in a:
    if a[i]!=None:
        d.update({i:a[i]})
print(d)