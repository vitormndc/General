def dumber(string):

    new_string = ''
    for c, i in enumerate(string):
        if c == 0:
            new_string = string[c].upper()
        else:
            if new_string[c-1].isupper():
                new_string += string[c].lower()
            else:
                new_string += string[c].upper()
    return new_string
