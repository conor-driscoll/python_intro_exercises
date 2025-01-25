numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

def remainders_3(numbers):
    return [number % 3 for number in numbers]

#prints argument if >=1 element isn't evenly divisible by 3
def divisible_by_3_test(data_sets): 
    if any(remainders_3(data_sets)) == True:
        print (data_sets)

print('Lists that contain at least one number not divisible by 3:')
divisible_by_3_test(numbers_1)
divisible_by_3_test(numbers_2)
divisible_by_3_test(numbers_3)
divisible_by_3_test(numbers_4)