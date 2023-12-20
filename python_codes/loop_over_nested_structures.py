foods = [['apple', 'banana', 'orange'],
         ['carrot', 'cucumber', 'tomato']]
for items in foods:
    print(items) # prints the items in the list
    print("\n")
for items1 in foods[0]:
    print(items1)
    print("\n") # prints the items in the 1st list
for items in foods:
    print(items[0])
    print("\n")

pets = {
    'birds': {
        'parrot': 'Arthur',
        'canary': 'Ford'
    },
    'fish': {
        'goldfish': 'Zaphod',
        'koi': 'Trillian'
    }
}

for e in pets:
    print(e) # would only print keys 
for e in pets['birds']:
    print(e) # prints the keys in the key "bird"
for e in pets['birds'].values():
   print(e)

# below is a list of dictionaries
weather = [
    {
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'data': 'typo',
        'state': 'sunny',
        'temp': 74.8
    }
]

for e in weather[0]:
    print(e)

for e in weather[0].values():
    print(e)

for e in weather:
    print(e['date']) # this works bcs there are keys with same name in both dicts.
    print(e['state'])
    print(e['temp'])