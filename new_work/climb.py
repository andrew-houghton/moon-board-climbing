from hold import Hold

class Climb():
	def __init__(self,input_type,input_data):
		if input_type == 'json':
			self.holds = []
			for hold_text in input_data['Moves']:
				next_hold = Hold('website_format',hold_text)
				self.holds.append(next_hold)

			self.rating = input_data['UserRating']
			self.grade = input_data['Grade']
		else:
			raise ValueError('Invalid input type.')
