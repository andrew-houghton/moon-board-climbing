import pickle
all_data = pickle.load( open('mod_data.pickle', 'rb'))

# # Checking what holds exist
# row=set()
# col=set()
# for i in all_data:
# 	for j in all_data[i]['Moves']:
# 		col.add(j['Description'][0])
# 		row.add(j['Description'][1:])

# print(len(sorted(row)))
# print(sorted(row))
# print(len(sorted(col)))
# print(sorted(col))

# Encoding constants
move_seperator=','
grade_seperator='_'
climb_seperator='|'
num_base=96

def encode_move(move_str):
	# Turns a move from readable format to LSTM format.
	# EG G2 --> Gb
	return move_str[0]+chr(num_base+int(move_str[1:]))

def decode_move(move_str):
	return move_str[0]+str(ord(move_str[1])-num_base)

def character_represet(climb):
	# turns a climb loaded from a pickle file into LSTM format

	climb_moves=[]
	for move in climb['Moves']:
		climb_moves.append(encode_move(move['Description']))

	move_str = move_seperator.join(climb_moves)
	grade_str = grade_seperator + climb['Grade']

	return move_str + grade_str

def character_decode(climb_chars):
	# turns a climb formated for LSTM into a dictionary format

	moves,grade=climb_chars.split('_')
	move_list=moves.split(',')
	move_list=[decode_move(i) for i in move_list]

	return {
		'Grade':grade,
		'Moves':move_list
	}

# TEXT FILE SAVING

# climb_strings = [character_represet(all_data[i]) for i in all_data]

# filename='climbs2.txt'
# f=open(filename,'w')
# f.write(climb_seperator.join(climb_strings))
# f.close()

# IMAGE CODE
from PIL import Image

image_folder = 'png_climbs/'
test_name = 'climb{}.png'

def move_coords(moves):
	output_data=[]
	for move in moves:
		move_str=move['Description']
		output_data.append([
			ord(move_str[0])-65,
			int(move_str[1:])-2
			])
	return output_data

for i in all_data:
	image = Image.new('1', (11, 18))
	im = image.load()

	climb = all_data[i]
	for x,y in move_coords(climb['Moves']):
		im[x,y]=1

	print('Saved {} images'.format(i))

	image.save(image_folder+test_name.format(i))
