def binary_search(numbers_list, number):
    """Searches for a number in a sorted list, and returns the index
    of the list where the number was found, or -1 in case the number
    is not found.
    """
    section_start = 0
    section_end = len(numbers_list) - 1
    section_middle = section_end // 2

    while (number >= numbers_list[section_start]
            and number <= numbers_list[section_end]):
        if number <= numbers_list[section_middle]:
            section_end = section_middle
            section_middle = section_middle // 2
        else:
            section_start = section_middle
            section_middle = (section_end + section_middle) // 2

        if numbers_list[section_start] == number:
            return section_start
        if numbers_list[section_end] == number:
            return section_end

    return -1
