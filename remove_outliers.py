import pickle
all_data = pickle.load( open('mod_data.pickle', 'rb'))

new_data={}

valid,invalid = 0,0

for i in all_data:
	grade=int(all_data[i]['Grade'])
	if grade >= 4 and grade <= 14:
		if len(all_data[i]['Moves'])<=12 and len(all_data[i]['Moves'])>=5:
			valid+=1
			new_data[i]=all_data[i]
		else:
			invalid+=1
	else:
		invalid+=1

print('{} valid climbs\n{} invalid climbs'.format(valid,invalid))

pickle.dump(new_data, open('crop_data.pickle','wb'))
