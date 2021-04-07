def binary_search(numbers_list, number):
    """Searches for a number in a sorted list, and returns the index
    of the list where the number was found, or -1 in case the number
    is not found.
    """
    section_start = 0
    section_end = len(numbers_list) - 1
    section_middle = section_end // 2

    while section_start <= section_end:
        section_middle = section_start + (section_end - section_start) // 2
        if numbers_list[section_middle] == number:
            return section_middle
        elif numbers_list[section_middle] < number:
            section_start = section_middle + 1
        else:
            section_end = section_middle - 1

    return -1
