import pickle
all_data = pickle.load( open('mod_data.pickle', 'rb'))

x_vals=set()
y_vals=set()
for i in all_data:
	climb=all_data[i]

	for move in climb['Moves']:
		x=move['Description'][0]
		y=move['Description'][1:]
		x_vals.add(x)
		y_vals.add(y)

print(sorted(x_vals))
print(sorted(y_vals))

print('x len {} y len {}'.format(len(x_vals),len(y_vals)))