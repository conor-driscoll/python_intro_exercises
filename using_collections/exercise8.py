text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# The code on lines 3 & 4 produce different values, because the index value produced by the code on line 3 applies to the new string slice created, while the index value produced by the code on line 4 applies to the original string on line 1.