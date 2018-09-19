#! python
# Advent of Code - Day 01
#
#

import helpers.helpers as helpers


def captcha(number):
    number_str = str(number)

    couples = []

    i = 0
    j = 1
    while i < len(number_str) - 1:
        if number_str[i] == number_str[j]:
            couples.append(number_str[i])

        i += 1
        j += 1

    if number_str[0] == number_str[-1]:
        couples.append(number_str[0])

    # print(couples) #DEBUG

    return helpers.sum_of_list_values(couples)


captcha_number = helpers.read_as_string('number1.txt')

print(captcha(captcha_number))
