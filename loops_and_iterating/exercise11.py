my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index1 = 0

while index1 < len(my_list):
    index2 = 0
    while index2 < len(my_list[index1]):    
        number = my_list[index1][index2]
        if number % 2 == 0:
            print(number)
        index2 += 1
    index1 += 1

