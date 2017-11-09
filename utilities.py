
# Encoding constants
padding_character='_'
climb_seperator='|'
max_moves=13
num_base=96
grade_base=44

def encode_move(move_str):
	# Turns a move from readable format to LSTM format.
	# EG G2 --> Gb
	return move_str[0]+chr(num_base+int(move_str[1:]))

def encode_grade(grade_str):
	# Turns a grade from readable format to LSTM format.
	return chr(grade_base+int(grade_str))

def decode_move(move_str):
	return move_str[0]+str(ord(move_str[1])-num_base)

def decode_grade(grade_str):
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
	moves=climb_chars[:max_moves*2] #moves section of string
	grade=climb_chars[max_moves*2] #last character of string

	move_list=[]
	for i in range(0,max_moves*2,2): #go through the string in steps of 2
		current_move=climb_chars[i:i+2] #look at a pair of characters (a move)
		if current_move != '__': #don't process padding characters
			move_list.append(current_move)
	move_list=[decode_move(i) for i in move_list]

	return {
		'Grade':grade,
		'Moves':move_list
	}

def nn_grade_to_british(grade):
	#Must write +'s first'
	GradeConv = {
	'8B+': '16',
	'8B': '15',
	'8A+': '14',
	'8A': '13',
	'7C+': '12',
	'7C': '11',
	'7B+': '10',
	'7B': '9',
	'7A+': '8',
	'7A': '7',
	'6C+': '6',
	'6C': '5',
	'6B+': '4',
	'6A+': '2',
	'6A': '1'}