import utilities
import send_climb_data

filename='climb_text/climbs_out.txt'
f=open(filename,'r')
all_text = f.read()
climbs = [i for i in all_text.split(utilities.climb_seperator) if len(i) == utilities.max_moves*2+1]

# sort climbs based on last character in string
climbs = sorted(climbs, key=lambda x: int(x[-1]))

valid_climbs=[]
for i in range(len(climbs)):
	climb = utilities.character_decode(climbs[i])
	if utilities.is_valid_climb(climb):
		valid_climbs.append(climb)

climb_num=0
for i in range(len(valid_climbs)):
	climb = valid_climbs[i]
	if i%4==0:
		climb_save_name = 'Lstm_Gen0_Climb{}'.format(climb_num)
		print('saving climb {} with name {}'.format(climb_num,climb_save_name))
		send_climb_data.send_climb(climb,climb_save_name)
		climb_num+=1
