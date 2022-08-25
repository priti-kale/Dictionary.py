# Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
a={}
for i in(d1,d2):
    a.update(i)
for j in a:
    if j in d1:
        if j in d2:
            a.update({j:(d1[j]+d2[j])})  
print(a)              


