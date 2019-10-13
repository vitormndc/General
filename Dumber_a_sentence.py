def dumber(string):

    new_string = ''
    for c, i in enumerate(string):
        previous_letter = -1

        if c == 0:
            new_string = string[c].upper()

        else:
            while string[c+previous_letter] == ' ':  # if the last character is a space it will look for the last letter
                previous_letter += -1

            if new_string[c+previous_letter].isupper():
                new_string += string[c].lower()
            else:
                new_string += string[c].upper()

    return new_string
