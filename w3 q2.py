# 2. Write a Python script to add a key to a dictionary. Go to the editor

a={0: 10, 1: 20}
b={0: 10, 1: 20, 2: 30,30:2}
print(a)
a.update(b)
print(a)


dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
dict_3 = dict_2.copy()
dict_3.update(dict_1)
print(dict_3)
