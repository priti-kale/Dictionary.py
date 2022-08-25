# Q42.
# Write a Python program to check all values are same in a dictionary. Go to the 
# editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False



a={'Cierra Vega': 10, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
n=int(input("enter:"))
print(len(a))
c=0
for i in a:
    if a[i]==n:
        c=c+1
print(c)
if c==len(a):
    print(True)
else:
    print(False)
