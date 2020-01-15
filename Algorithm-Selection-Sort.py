def selection_sort(number_array):

    starting_point = 0

    while starting_point < len(number_array):

        min = number_array[starting_point]

        for count, item in enumerate(number_array):

            if count < starting_point:
                continue

            if item <= min:
                min = item
                min_index = count

        number_array.pop(min_index)
        number_array.insert(starting_point, min)
        starting_point += 1

    return number_array
