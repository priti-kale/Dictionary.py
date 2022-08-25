
# Q46.Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

# a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# d={}
# for i in a:
#     for j in i:
#         d.update({j:int(i[j])})
# print(d)

a=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

d={}
for i in a:
    for j in i:
        d.update({j:float(i[j])})
print(d)