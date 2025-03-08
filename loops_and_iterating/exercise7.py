my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# def find_integers(my_collection):
#     integer_list = []
#     for element in my_collection:
#         if type(element) is int:
#             integer_list.append(element)
#     return integer_list

def find_integers(my_collection):
    return [ element 
             for element in my_collection
             if type(element) is int ]

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]


