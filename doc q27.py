
a = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

for i in a:
    print(i,end=" ")
l1=list(a.values())
print()
for i in range(len(l1)):
    for j in range(len(l1)):
        d=l1[j][i]
        print(d,end=" ")
    print()