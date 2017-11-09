from PIL import Image

file_path='./hypergan/samples/'
image_name = '002054.png'
black_threshold = 100
default_grade='6C+'

image = Image.open(file_path+image_name)
image = image.convert('L')
image = image.point(lambda x: 0 if x<black_threshold else 255, '1')
# image.show()

num_sample_cols=5
num_sample_rows=2
image_size=18

def process_img(im):
	pixels = list(im.getdata())
	width, height = im.size
	pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

	holds=[]

	for y in range(len(pixels)):
		row=pixels[y]
		for x in range(len(row)):
			if pixels[y][x]:
				holds.append(chr(65+x) + str(18-y))

	return list(reversed(holds))

climb_num=0

for row in range(num_sample_rows):
	top_y=image_size*row
	for col in range(num_sample_cols):
		top_x=image_size*col

		current_image = image.crop((
			top_x,
			top_y,
			top_x+image_size,
			top_y+image_size))

		# current_image.show()
		moves = process_img(current_image)

		climb = {
			'Grade':default_grade,
			'Moves':moves
			}

		climb_save_name = 'HyperGAN_Gen0_Climb{}'.format(climb_num)
		print('saving climb {} with name {}'.format(climb_num,climb_save_name))
		print(climb)
		climb_num+=1