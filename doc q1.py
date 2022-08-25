Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',
                'P 0 3 ': 'Soft Computing'}

d={}
for i,j in Product_list.items():
    for x in " ":
        i=i.replace(x,"")
        print(i)
        d[i]=j
print(d)
