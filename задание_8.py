def transformation():
    """
    Reads a string, converts it to a list of characters,
    sorts them, and returns the sorted string.
    :line: A string as an argument
    :return: Sorted string
    """
    line = input()
    lst = list(line)
    lst.sort()

    return ''.join(lst)

