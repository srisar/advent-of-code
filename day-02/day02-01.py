#! python
# Advent of Code - Day 02
#
# The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on
# the right track, they need you to calculate the spreadsheet's checksum. For each row, determine
# the difference between the largest value and the smallest value;
# the checksum is the sum of all of these differences.
#
# For example, given the following spreadsheet:
# 5 1 9 5
# 7 5 3
# 2 4 6 8
#
# The first row's largest and smallest values are 9 and 1, and their difference is 8.
# The second row's largest and smallest values are 7 and 3, and their difference is 4.
# The third row's difference is 6.

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
