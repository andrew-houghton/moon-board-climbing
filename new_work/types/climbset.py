from climb import Climb

class ClimbSet():
	def __init__(self, climbs):
		if not type(climbs)==list:
				raise ValueError('Input must be a list of climb objects. Please input a list.')

		for climb in climbs:
			if type(climb) != Climb:
				raise ValueError('Objects in climbset must be of type climb.')

		self.climbs = climbs

	def pre_grade_string(self):
	def post_grade_string(self):
	def no_grade_string()
