dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# This code will print: [1, 42, 3]
# This is because the mutation performed on
# line 7, was performed on a nested list within
# the original dict1, so therefore, this mutation will be
# reflected in its shallow copy, dict2. 