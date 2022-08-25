# Write a Python program to remove a specified dictionary from a given list. 
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
#  {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

# Remove id #FF0000 from the said list of dictionary:

# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},
#  {'id': '#808000', 'color': 'Olive'}]



a=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
{'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
b=[]
for i in a:
    # print(i)
    b={}
    c=0
    for j in i: 
        if i[j]!="#FF0000":
            c=c+1
    if c==len(i):
        l={}
        for k in i:
            l.update({k:i[k]})
    b.append(l)
print(b)
            
        
