#! python
# Advent of Code - Day 01
#
# The captcha requires you to review a sequence of digits (your puzzle input) and
# find the sum of all digits that match the next digit in the list. The list is circular,
# so the digit after the last digit is the first digit in the list.

# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2)
# matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

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
