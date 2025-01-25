numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

def remainders_5(numbers):
    return [number % 5 for number in numbers]

#prints argument if 0 #s are evenly divisible by 5
def divisible_by_5_test(data_sets): 
    if all(remainders_5(data_sets)) == True:
        print (data_sets)

print('Lists that contain 0 numbers which are evenly divisible by 5:')
divisible_by_5_test(numbers_1)
divisible_by_5_test(numbers_2)
divisible_by_5_test(numbers_3)
divisible_by_5_test(numbers_4)