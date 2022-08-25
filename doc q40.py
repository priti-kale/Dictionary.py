# Q40. Write a Python program to convert more than one list to nested dictionary. 

# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]


d1=['S001', 'S002', 'S003', 'S004']
d2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
d3=[85, 98, 89, 92]
a={}
for i in range(len(d1)):
    a.update({d1[i]:{d2[i]:d3[i]}})
print(a)