# Q51.Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:


a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
d={}
for i in a:
    b=[]
    for j in a[i]:
        if j%2==0:
            b.append(j)
    d.update({i:b})
print(d)
