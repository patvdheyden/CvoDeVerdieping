def get_input( prompt ):
    value = input( prompt )
    for letter in value:
        if letter < 'a' or letter > 'z':
            print( "The character", letter, "is not allowed!")
            value = get_input( prompt ) # DO NOT DO THIS!
    return value

s = get_input( "Give a string of lower case letters: " )
print( "The user entered:", s )