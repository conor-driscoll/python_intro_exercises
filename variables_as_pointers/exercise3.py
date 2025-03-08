dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])
 
# This code will print: 'The Life of Brian'
# This is because the 'Holy Grail'
# mutation was performed in the
# outermost layer of the shallow copy dict2, 
# on an immutable data type, so therefore,
# this mutation won't be reflected in the original, dict1. 