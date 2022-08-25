# Q18.Write a Python program to get the maximum and minimum value in a dictionary.


a={'gaurav':97,"kachru":54,"976":84}
max=0
min=a["gaurav"]
for i in a:
    if a[i]>max:
        max=a[i]
    if a[i]<min :
        min=a[i]
print(max)
print(min)
