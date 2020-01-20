def merge_sort(number_array):
    middle = int(len(number_array) / 2)

    left_side = number_array[middle:]
    right_side = number_array[:middle]

    number_array.clear()

    while left_side and right_side:

        min_left = left_side[0]
        min_right = right_side[0]

        for i in left_side:
            if i < min_left:
                min_left = i

        for i in right_side:
            if i < min_right:
                min_right = i

        if min_left < min_right:
            min_left = left_side.pop(left_side.index(min_left))
            number_array.append(min_left)

        else:
            min_right = right_side.pop(right_side.index(min_right))
            number_array.append(min_right)

    return number_array
