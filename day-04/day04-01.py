#! python
# Advent of Code - Day 04
#
# A new system policy has been put in place that requires all accounts to use a passphrase
# instead of simply a password. A passphrase consists of a series of words
# (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
#
# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.

import helpers.helpers as helpers


def is_valid_passphrase(phrase):
    plist = phrase.split(' ')


#

data = helpers.read_as_list('day04.txt')

count = 0
for phrase in data:
    if is_valid_passphrase(phrase):
        count += 1

print("valid passphrases", count)
