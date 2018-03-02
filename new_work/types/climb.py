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

	def as_image(self):
		from PIL import Image
		
		# Create new blank canvas
		image = Image.new('1', (18, 18))
		
		im = image.load()

		# Add all the holds to the image
		for hold in self.holds:
			# Subtract 1 to convert row and col to 0 indexed values
			# Subtract from 18 because row 1 is at the bottom
			pixel_y = 18-(hold.row)
			pixel_x = hold.col-1
			im[pixel_x,pixel_y]=1

		# Note: use .save to save the image.
		return image