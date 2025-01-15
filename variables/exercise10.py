obj = 'ABcd'       # reassignment
obj.upper()        # neither
obj = obj.lower()  # reassignment
print(len(obj))    # neither
obj = list(obj)    # reassignment
obj.pop()          # mutation
obj[2] = 'X'       # mutation
obj.sort()         # mutation
set(obj)           # neither
obj = tuple(obj)   # reassignment