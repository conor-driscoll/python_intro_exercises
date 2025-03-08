set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# This code will print the edited value of set1:
# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}
# This is because set2 & set1 share this set as their reference object.