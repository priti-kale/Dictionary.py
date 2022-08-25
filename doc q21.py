
d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
 {"V":"S009"},{"VIII":"S007"}]
 
l1=[]
for i in d1:
    for x,y in i.items():
        if y not in l1:
            l1.append(y)
print (l1)