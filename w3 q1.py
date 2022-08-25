a={'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
# d={1:2,3:4,4:3,2:1,0:0}
# l=list(d.items())
# l.sort()
# print('Ascending order is',l)
# l=list(d.items())
# l.sort(reverse=True)
# print('Descending order is',l)
# l=list(a.items())
# l.sort()
# print(l)
# l=list(a.items())
# l.sort(reverse=True)
# print(l)

# print(sort(d))


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items())
print('Dictionary in ascending order by value : ',sorted_d)