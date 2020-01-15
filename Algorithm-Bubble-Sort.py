def bubble_sort(number_array):

    reference = []

    while number_array != reference:

        reference = number_array.copy()

        for count, item in enumerate(number_array):

            if count == 0:
                continue

            if number_array[count] < number_array[count-1]:
                number_array[count], number_array[count-1] = number_array[count-1], number_array[count]

    return number_array
