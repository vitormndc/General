'''
The lc function needs two lists to work, the first one is the list you wanna clean,
and the second is the characters you want to remove from itens in the first list.
'''
cleaned_list = []

def lc(my_list, remove):

    for iten in my_list:
        iten = str(iten)

        for symbol in remove:
            symbol = str(symbol)

            if symbol in iten:
                iten = iten.replace(symbol, '')
            else:
                pass

        cleaned_list.append(iten)

    return cleaned_list

