number_input = int(input('Even vs odd assessor: \nPlease submit an integer '))

def even_or_odd(integer1):
    if integer1 % 2 == 0:
        print('even')
    else: print('odd')

even_or_odd(number_input)