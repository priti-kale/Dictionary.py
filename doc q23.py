a={'C': 45, 'B': 23, 'D': 56, 'A': 67, 'E': 12, 'F': 69} 

# F  : 69  
# A  : 67  
# D  : 56

max=0
sec_max=0
thrid_max=0
for i in a:
    for j in a:
        if a[j]>max:
            max=a[j]
        if a[j]>sec_max and a[j]!=max:
            sec_max=a[j]
        if a[j]>thrid_max and a[j]!=sec_max and a[j]!=max:
            thrid_max=a[j]
print(max)
print(sec_max)
print(thrid_max)