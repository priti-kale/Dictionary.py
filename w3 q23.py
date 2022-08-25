# 23. Write a Python program to combine values in python list of dictionaries. Go to 
# the editor
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
# {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})


L = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d = {}
for i in L:
    key = i['item']
    print(key)
    value = i['amount']
    print(value)

    if key not in d.keys():
        k = {key:value}
        d.update(k)
        print(d)
    else:
        d[key] += value
        print(d)
print(d)