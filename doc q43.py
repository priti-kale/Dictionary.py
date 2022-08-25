# Q43.Write a Python program to create a dictionary grouping a sequence of 
# key-value pairs into a dictionary of lists. 
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}




a = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
for i in a:
    # print(i)
    if i[0] not in d.keys():
        d.update({i[0]:[i[1]]})
    elif i[0] in d.keys():
        d[i[0]].append(i[1])
print(d)
