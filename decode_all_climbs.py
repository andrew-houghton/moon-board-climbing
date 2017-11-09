import utilities

filename='climb_text/climbs_out.txt'
f=open(filename,'r')
all_text = f.read()
climbs = [i for i in all_text.split(utilities.climb_seperator) if len(i) == utilities.max_moves*2+1]

# sort climbs based on last character in string
climbs = sorted(climbs, key=lambda x: int(x[-1]))

for i in range(len(climbs)):
	climb = utilities.character_decode(climbs[i])
	if utilities.is_valid_climb(climb):
		print(climb)
		if i%4==0:
			climb_save_name = 'Lstm_Gen0_Climb{}'.format(i)
			print('saving climb {} with name {}'.format(i,climb_save_name))
