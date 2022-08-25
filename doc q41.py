# Q41.Write a Python program to filter the height and width of students,
#  which are stored in a dictionary. 
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 
# 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 651), 'Kierra Gentry':(6.0, 68), 
'Pierre Cox': (5.8, 66)}
d={}
for i in a:
    k=a[i]
    if k[0]>6 and k[1]>=70:
        d.update({i:(k[0],k[1])})
print(d)



