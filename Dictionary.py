# Dictionary

import json
from difflib import get_close_matches # this library helps to get close matches...you can also import it as from difflib import grt_close_matches



data = json.load(open('data.json'))

# to check if the data is loaded
print(data['song'])


def translate (word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print('Did you mean %s instead' %get_close_matches(word,data.keys())[0])
        decide = input('press y for yes and n for no')
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return 'The word does not exist'
        else:
            return 'You have entered wrong input'



    else:
        print('Word doesnt exist inthis dictionary')



word = input('Type the word you want to search for')
output = translate(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)