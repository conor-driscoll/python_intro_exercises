input_number = int(input('Welcome to the Ryan O\'Reilly FACTORial machine...\n'
                         'Please enter a positive integer\n'
                         'to receive your FACTORial --> '))

def factorial_function(n):
    product = 1
    for factor in range(1, n + 1):
        product *= factor
    return product

print(factorial_function(input_number))