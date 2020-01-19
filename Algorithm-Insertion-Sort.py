def insertion_sort(number_array):

    for count, item in enumerate(number_array):

        if count == 0:
            continue

        while number_array[count] < number_array[count - 1]:
            number_array[count], number_array[count - 1] = number_array[count - 1], number_array[count]
            count -= 1

            if count == 0:
                break

    return number_array
