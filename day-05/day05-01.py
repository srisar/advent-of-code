#! python
# Advent of Code - Day 04
#
# The message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction,
# and 2 skips the next one. Start at the first instruction in the list.
# The goal is to follow the jumps until one leads outside the list.
#
# In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1.
# So, if you come across an offset of 3, you would move three instructions forward,
# but change it to a 4 for the next time it is encountered.

# For example, consider the following list of jump offsets:
#
# 0
# 3
# 0
# 1
# -3
#
# Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this example,
# these offset values will be written all on one line, with the current instruction marked in parentheses.
# The following steps would be taken before an exit is found:
#
# (0) 3  0  1  -3  - before we have taken any steps.
# (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all).
#                       Fortunately, the instruction is then incremented to 1.
#  2 (3) 0  1  -3  - step forward because of the instruction we just modified.
#                       The first instruction is incremented again, now to 2.
#  2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
#  2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
#  2  5  0  1  -2  - jump 4 steps forward, escaping the maze.


import helpers.helpers as helpers


def jump_counter(lst):
    # setting the initial jump count
    jump_count = 0

    # setting the initial positional value
    pos = 0

    # length of the list.
    length = len(lst)

    print("number of items in list:", length)  # DEBUG

    while True:
        # get the current value
        current_val = lst[pos]

        print("current pos:", pos)
        print("current val:", current_val)

        # increase the current position value by 1
        lst[pos] = current_val + 1
        print("new val:", lst[pos])

        # change the new pos to be the current value
        pos = pos + current_val
        print("new pos:", pos)

        jump_count += 1

        if pos >= length or pos < 0:
            break

        print("\n")  # DEBUG

    return jump_count


# start of program

lst = helpers.read_as_list_numbers('day05-01.txt')

print("jump counts:", jump_counter(lst))
