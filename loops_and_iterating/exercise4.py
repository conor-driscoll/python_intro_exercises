my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    if number % 2 == 0:
        print(number)
    index += 1
print()
for number in my_list:
    if number % 2 == 1:
        print(number)