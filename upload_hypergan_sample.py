from PIL import Image

file_path='./hypergan/samples/'
image_name = '002054.png'

image = Image.open(file_path+image_name)
image.show()

num_sample_cols=8
num_sample_rows=3
image_size=18

for i in range()