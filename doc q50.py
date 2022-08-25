# Q50.Write a Python program to convert a given dictionary into a list of lists. 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:


a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d=[]
for i in a:
    d.append([i,a[i]])
print(d)