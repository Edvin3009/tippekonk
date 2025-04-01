# The Mecca of ugly code

import json
import api

with open('contestants.json', encoding='utf8') as f:
        contestants = json.load(f)

tabledata = api.getTable()
table = {}
i = 1
for team in tabledata:
    table[team['team']] = i
    i += 1

conts = contestants['contestants']

guesses = []
for i in range(len(conts)):
    guesses.append(conts[i]['guess'])

i = 0
for guess in guesses:
    contestants['contestants'][i]['points'] = []
    j = 1
    for team in guess:
        contestants['contestants'][i]['points'].append(abs(j - table[guess[j-1]]))
        j += 1
    i += 1

def get_contestants_data():
    return contestants

         