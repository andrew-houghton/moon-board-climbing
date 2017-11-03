import pickle
import pprint
import re

def multiwordReplace(text, wordDic):
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)

#Must write +'s first'
GradeConv = {
'8B+': '16',
'8B': '15',
'8A+': '14',
'8A': '13',
'7C+': '12',
'7C': '11',
'7B+': '10',
'7B': '9',
'7A+': '8',
'7A': '7',
'6C+': '6',
'6C': '5',
'6B+': '4',
'6A+': '2',
'6A': '1'}

pp = pprint.PrettyPrinter(indent=4)
all_data = pickle.load(open('C:/Users/Ryan/Desktop/MBP/all_data.pickle', 'rb'))
mod_data = {}

print('Number of climbs in dataset = {}'.format(len(all_data)))
print('Printing out all info about the first climb;')

for x in range(0, len(all_data)):
    mod_data[x] = {}
    mod_data[x]["Grade"] = multiwordReplace(all_data[x]["Grade"], GradeConv)
    mod_data[x]["Moves"] = all_data[x]["Moves"]
    for y in range(0, len(mod_data[x]["Moves"])):
        del mod_data[x]["Moves"][y]["Id"]
    mod_data[x]["UserRating"] = all_data[x]["UserRating"]

pickle.dump(mod_data, open('C:/Users/Ryan/Desktop/MBP/mod_data.pickle','wb'))
