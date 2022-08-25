# Q33.Python: Print a dictionary line by line

a = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for i in a:
    for j in a[i]:
        # print(a[i][j])
        print(j,":",a[i][j])

