import load_json_climbs
from pathlib import Path

def create_lstm_strings():
	base_climbset = load_json_climbs.load_all_as_climbset()

image = Image.new('1', (18, 18))
im = image.load()

for x, y in move_coords(climb['Moves']):
    im[x, y] = 1
image.save(image_folder + grade_folder + test_name.format(i))
