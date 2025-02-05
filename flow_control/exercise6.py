input_string = input('Converts to CAPS if >10 characters (incl. spaces)... \n'
                     'Please enter text: ')

# def over10_chr_uppercase_converter(string1):
    # if len(string1) > 10:
        # return string1.upper()
    # else:
        # return string1

def over10_chr_uppercase_converter(string1):
    return(string1.upper() if len(string1) > 10 else string1)

print(over10_chr_uppercase_converter(input_string))