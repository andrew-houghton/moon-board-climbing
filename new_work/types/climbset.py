from climb import Climb

terminator_character = '_'

class Climbset():
	def __init__(self, climbs):
		if not type(climbs)==list:
				raise ValueError('Input must be a list of climb objects. Please input a list.')

		for climb in climbs:
			if type(climb) != Climb:
				raise ValueError('Objects in climbset must be of type climb.')

		self.climbs = climbs

	def __init__(self):
		self.climbs = []

	def add(self,climb):
		if type(climb) != Climb:
			raise ValueError('Objects in climbset must be of type climb.')
		self.climbs.append(climb)

	def pre_grade_string(self):
		output_str = ''
		for climb in self.climbs:
			output_str+=climb.grade.as_nn_grade()
			output_str+=climb.moves_nn_string()
		return output_str
		

	def post_grade_string(self):
		output_str = ''
		for climb in self.climbs:
			output_str+=climb.moves_nn_string()
			output_str+=climb.grade.as_nn_grade()
		return output_str
		

	def no_grade_string(self):
		output_str = ''
		for climb in self.climbs:
			output_str+=climb.moves_nn_string()
			output_str+=terminator_character
		return output_str
		
