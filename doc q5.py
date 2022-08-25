# Write a Python program to sort (ascending and descending) a dictionary by value.

dic= {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=[]
c={}
for i in dic:
    a.append(dic[i])
for j in range(len(a)):
    for k in range(len(a)-1):
        if a[k]>a[k+1]:
            t=a[k]
            a[k]=a[k+1]
            a[k+1]=t
for m in range(len(a)):
    for l in dic :
        if dic[l]==a[m]:
            c.update({m:a[m]})
print(c)
        

