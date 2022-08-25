# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd


a={'1':['a','b'], '2':['c','d']}
result = ''
list_1 = a['1']
list_2 = a['2']
for i in list_1:
    for j in list_2:
        result = i + j
        print(result)