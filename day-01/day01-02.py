#! python
#

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
