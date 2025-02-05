integer_input = int(input('Welcome to the integer sorter \n'
                      'Please submit an integer: '))

# I eventually realized that the invalid syntax error that the code below produces, is due to the fact this match statement was introduced in Python 3.10, and I was attempting to run it with 3.9.6.
# 
# def integer_sorter(integer):
#     match integer:
#         case 0 <= integer <= 50:
#             print('The value is between 0 and 50, inclusive.')
#         case 51 <= integer <= 100:
#             print('The value is between 51 and 100, inclusive.')
#         case integer > 100:
#             print('The value is greater than 100.')
#         case _:
#             print('The value is less than 0.')

def integer_sorter(integer):
    if integer < 0:
        print(f'{integer} is less than 0.')
    elif integer < 51:
        print(f'{integer} is between 0 and 50, inclusive.')
    elif integer < 101:
        print(f'{integer} is between 51 and 100, inclusive.')
    else:
        print(f'{integer} is greater than 100.')

integer_sorter(integer_input)