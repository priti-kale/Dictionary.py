# a=['gaurav','riti','priti','kale']
# b=[1,2,3,4]
# d={}


keys_1 = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
d1 = {}
for i in range (len(keys_1)):
    d1.update({keys_1[i]:values[i]})
print(d1)