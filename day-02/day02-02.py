#! python
# Advent of Code - Day 02
#
# "Based on what we're seeing, it looks like all the User wanted is some information
# about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped
# for that kind of calculation - most of us specialize in bitwise operations."
#
# It sounds like the goal is to find the only two numbers in each row where one
# evenly divides the other - that is, where the result of the division operation is a whole number.
# They would like you to find those numbers on each line, divide them, and add up each line's result.
#
# For example, given the following spreadsheet:
# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
#
# In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
# In the second row, the two numbers are 9 and 3; the result is 3.
# In the third row, the result is 2.

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
