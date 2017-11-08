import pickle
all_data = pickle.load( open('mod_data.pickle', 'rb'))

# Encoding constants
padding_character='_'
climb_seperator='\n'
max_moves=12
num_base=96
grade_base=47

def encode_move(move_str):
	# Turns a move from readable format to LSTM format.
	# EG G2 --> Gb
	return move_str[0]+chr(num_base+int(move_str[1:]))

def encode_grade(grade_str):
	# Turns a grade from readable format to LSTM format.
	return chr(grade_base+int(grade_str))

def decode_move(move_str):
	return move_str[0]+str(ord(move_str[1])-num_base)

def decode_move(grade_str):
	return str(ord(grade_str)-grade_base)

def character_represet(climb):
	# turns a climb loaded from a pickle file into LSTM format

	climb_moves=[]
	for move in climb['Moves']:
		climb_moves.append(encode_move(move['Description']))

	#create a string from moves
	move_str = ''.join(climb_moves)

	#pad and crop the string
	move_str = move_str[:2*max_moves].ljust(2*max_moves,padding_character)

	#create the grade string
	grade_str = encode_grade(climb['Grade'])

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

climb_strings = [character_represet(all_data[i]) for i in all_data]

filename='padded_climbs.txt'
f=open(filename,'w')
f.write(climb_seperator.join(climb_strings))
f.close()
