import pickle
import utilities

all_data = pickle.load(open('pickles/crop_data.pickle', 'rb'))

# TEXT FILE SAVING
climb_strings = [utilities.character_represet(all_data[i]) for i in all_data]

filename = 'climb_text/padded_climbs.txt'
f = open(filename, 'w')
f.write(utilities.climb_seperator.join(climb_strings))
f.close()
