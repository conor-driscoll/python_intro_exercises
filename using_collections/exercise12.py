numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

def three_detector(test_collection):
    print(3 in test_collection)

three_detector(numbers1)
three_detector(numbers2)
three_detector(numbers3)
three_detector(numbers4)
three_detector(numbers5)