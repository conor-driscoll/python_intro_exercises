def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# This function creates an alphabetically sorted list of 
# the keys of my_dict, and then the 2nd element in the list
# is selected and an upper-cased version of this string
# is created, and finally, returned.
# Output value:
# CHRIS