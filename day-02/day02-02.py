#! python
#

import helpers.helpers as helpers


def convent_raw_data(rdata):
    """Convert each line of text input into int numbers of list"""
    data = []

    for line in rdata:
        s_line = line.split('\t')
        data.append([int(x) for x in s_line])

    return data


def find_even_divisible_in_list(data):
    """Find divisible numbers in a whole data list"""
    return [even_divisible(line) for line in data]


def even_divisible(lst):
    """Find two numbers that can evenly divide other"""
    i = 0
    while i < len(lst):

        j = 0
        while j < len(lst):
            if i != j:
                if lst[i] % lst[j] == 0:
                    return [lst[i], lst[j]]
            j += 1
        i += 1


def divide_and_sum(lst):
    """Divide the numbers in list and add them together"""
    total = 0

    for data in lst:
        total += int(data[0] / data[1])

    return total


#
#
raw_data = helpers.read_as_list('day02-02-data.txt')

d = convent_raw_data(raw_data)

print(divide_and_sum(find_even_divisible_in_list(d)))
