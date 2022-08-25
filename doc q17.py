# Q17.Write a Python program to sort a dictionary by key.



color_dict = {'red':'#FF0000',
	          'green':'#008000',
	          'black':'#000000',
	          'white':'#FFFFFF'}
b={}
# a.sorted(color_dict.item())
b=dict(sorted(color_dict.items()))
print(b)