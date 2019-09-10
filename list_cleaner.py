cleaned_list = []

def lc(my_list, remove):

    for item in my_list:
        item = str(item)

        for symbol in remove:
            symbol = str(symbol)

            if symbol in item:
                item = item.replace(symbol, '')
            else:
                pass

        cleaned_list.append(item)

    return cleaned_list
