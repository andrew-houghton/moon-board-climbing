from hold import Hold
from grade import Grade

def _process_grade(grade):
	return

class Climb():
	def __init__(self,input_type,input_data):
		if input_type == 'json':
			self.holds = []
			for hold_text in input_data['Moves']:
				next_hold = Hold('website_format',hold_text)
				self.holds.append(next_hold)

			self.rating = input_data['UserRating']
			self.grade = Grade(input_data['Grade'])
		else:
			raise ValueError('Invalid input type.')

	def moves_nn_string(self):
		return ''.join([hold.as_nn_format() for hold in self.holds])