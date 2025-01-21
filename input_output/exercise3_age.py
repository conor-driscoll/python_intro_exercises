age = int(input('How old are you? '))
interval = 10
print()
print(f'You are {age} years old.')
while interval <= 40:
    print(f'In {interval} years, you will be {age + interval} years old.')
    interval += 10