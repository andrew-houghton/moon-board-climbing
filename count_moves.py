import pickle
from collections import Counter

all_data = pickle.load( open('crop_data.pickle', 'rb'))

# print(all_data[0])

# Checking what ratings exist
ratings=[]
for i in all_data:
	ratings.append(all_data[i]['UserRating'])

print('Ratings')
print(Counter(ratings))

# Checking what move counts exist
moves=[]
for i in all_data:
	moves.append(len(all_data[i]['Moves']))
print('Moves')
move_count=Counter(moves)
print(move_count)

# Checking what grades exist
grades=[]
for i in all_data:
	grades.append(all_data[i]['Grade'])
print('Grades')
print(Counter(grades))

for i in sorted(move_count):
	print('{} climbs with {} moves'.format(move_count[i],i))