#! python
# Advent of Code - Day 02
#
#

import helpers.helpers as helpers


def convert_raw_data(rdata):
    """Convert raw lines of data into list of numbers."""
    data = []

    for line in raw_data:
        raw_line = line.split('\t')
        new_line = []
        for item in raw_line:
            new_line.append(int(item))

        data.append(new_line)

    return data


def find_low_high(lst):
    low = lst[0]
    high = lst[0]

    for number in lst:
        if number < low:
            low = number
        if number > high:
            high = number

    return [low, high]


def find_checksum(lst):
    total = 0
    for line in lst:
        diff = line[1] - line[0]
        total += diff

    return total


#
#
raw_data = helpers.read_as_list('day02-01.txt')

number_data = convert_raw_data(raw_data)

low_high = []

for row in number_data:
    low_high.append(find_low_high(row))

checksum = find_checksum(low_high)

print(checksum)
