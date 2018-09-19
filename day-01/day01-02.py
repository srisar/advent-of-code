#! python
# Advent of Code - Day 01
#
# Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
# That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps
# forward matches it. Fortunately, your list has an even number of elements.
#
# 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
# 1221 produces 0, because every comparison is between a 1 and a 2.
# 123425 produces 4, because both 2s match each other, but no other digit has a match.
# 123123 produces 12.
# 12131415 produces 4.

import helpers.helpers as helper


def split_list(lst):
    """Splitting the list into two
    ex. [1,2,3,4,5,6] => [1,2,3], [4,5,6]"""

    return lst[:len(lst) // 2], lst[len(lst) // 2:]


def captcha(number):
    lists = split_list(str(number))

    # print(lists)  # DEBUG

    first_list = lists[0]
    second_list = lists[1]

    matched = []

    index = 0
    while index < len(first_list):
        if first_list[index] == second_list[index]:
            matched.append(first_list[index])
        index += 1

    total = 0
    for item in matched:
        total += int(item)

    return total * 2


#
#

number = helper.read_as_string('number2.txt')
print(captcha(number))
