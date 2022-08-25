
# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# a= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 35}
# for i in a:
#     c=0
#     for j in a:
#         if a[i]==a[j]:
#             c=c+1
#     if c>1:
#         print(i,a[i])
    
a= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
sec_max=0
thrid_max=0
for i in a:
    for j in a:
        if a[j]>max:
            max=a[j]
            max_k=j
        if a[j]>sec_max and a[j]!=max:
            sec_max=a[j]
            sec_k=j
        if a[j]>thrid_max and a[j]!=sec_max and a[j]!=max:
            thrid_max=a[j]
            thrid_k=j
print(max_k,max)
print(sec_k,sec_max)
print(thrid_k,thrid_max)

