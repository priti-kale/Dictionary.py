

a=[1,2,3]
b=["priti","gaurav","nikita"]
d={}
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            d.update({a[i]:b[j]})
print(d)