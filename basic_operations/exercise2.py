import math
Number = 4936
one_place = Number % 10
tens_place = int((Number % 4906) / 10)
hundreds_place = int((Number % 4036) / 100)
thousands_place = Number // 1000

print('1.', one_place)
print('2.', tens_place)
print('3.', hundreds_place)
print('4.', thousands_place)