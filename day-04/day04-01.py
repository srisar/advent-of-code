#
#

import helpers.helpers as helpers


def is_anagram(a, b):
    """checks if two strings are anagram"""
    if len(a) == len(b):
        for i in a:
            if i not in b:
                return False
        return True
    else:
        return False


def has_anagram(lst):
    """checks if list of strings has any anagram in them"""
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if len(lst[i]) == len(lst[j]):
                print("potential anagram pair:", lst[i], lst[j])

                if i != j and is_anagram(lst[i], lst[j]):
                    print("found:", [lst[i], lst[j]])
                    return [lst[i], lst[j]]
            j += 1
        i += 1
    return None


# program starts here
#
data = helpers.read_as_list('day04.txt')

valid = 0
invalid = 0
for line in data:
    line = line.rstrip('\n').split(' ')

    print("line:", line)

    if has_anagram(line) is not None:
        print("anagram pair:", has_anagram(line))
        invalid += 1
    else:
        print("valid line")
        valid += 1
    print("\n\n")

print("total pass phrases", len(data))
print("valid", valid)
print("invalid", invalid)
