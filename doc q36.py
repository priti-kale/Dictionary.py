
# Q36.Write a Python program to match key values in two dictionaries. 
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
# a={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# for i in a:
#     print(i)

d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}
d3={}
for i,j in d1.items():
    for x,y in d2.items():
        if i==x and j==y:
            print({i:j})
