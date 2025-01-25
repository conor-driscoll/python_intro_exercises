first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

def multiply_two_numbers(number1, number2):
    return number1 * number2

product = multiply_two_numbers(first_number, second_number)

print(f'{first_number} * {second_number} = {product}')
