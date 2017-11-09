import utilities

filename='climb_text/climbs_out.txt'
f=open(filename,'r')
all_text = f.read()
climbs = [i for i in all_text.split(utilities.climb_seperator) if len(i) == utilities.max_moves*2+1]

# sort climbs based on last character in string
climbs = sorted(climbs, key=lambda x: int(x[-1]))

for i in climbs:
	climb = utilities.character_decode(i)
	print(climb)