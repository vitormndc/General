'''
The lc function needs two lists to work, the first one is the list you wanna clean,
and the second is the characters you want to remove from itens in the first list.
'''
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
