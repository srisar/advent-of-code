def sum_of_list_values(lst):
    """Add all the values in the list"""

    total = 0
    for i in lst:
        total += int(i)

    return total


def read_as_string(file, line=1):
    """Open and read first line of text"""

    f = open(file, 'r')
    line = f.readline()
    f.close()

    return line


def read_as_list(file):
    """Open and read file and return each line
    as an item in the list"""

    f = open(file, 'r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]
    f.close()

    return lines


def read_as_list_numbers(file):
    f = open(file, 'r')
    lines = f.readlines()
    lines = [int(line.strip('\n')) for line in lines]
    f.close()

    return lines
