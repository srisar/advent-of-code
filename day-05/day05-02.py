#! python
# Advent of Code - Day 04
#
# Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1.
# Otherwise, increase it by 1 as before.
#
# Using this rule with the above example, the process now takes 10 steps, and the offset
# values after finding the exit are left as 2 3 2 3 -1.
#
# NOTE ON DEBUG LINES: Enabling the print() inside the loop considerably increases the computation time.
#
# total loop jumps: 25,136,209 (~25 millions)
#
# without single print() statement in the loop
# time taken: 5.869415283203125
#
# with one print() statement every 10000 iterations
# time taken: 12.29151463508606
#
# with one print() every iterations
# time taken: 344.89463233947754


import helpers.helpers as helpers
import time

start_time = time.time()


def jump_counter(lst):
    # setting the initial jump count
    jump_count = 0

    # setting the initial positional value
    pos = 0

    # length of the list.
    length = len(lst)

    print("number of items in list:", length)  # DEBUG

    x = 0
    while True:
        # get the current value
        current_val = lst[pos]

        # print("current pos:", pos) # DEBUG
        # print("current val:", current_val) # DEBUG

        if current_val >= 3:
            lst[pos] = current_val - 1
        else:
            lst[pos] = current_val + 1

        # print("new val:", lst[pos]) # DEBUG

        # change the new pos to be the current value
        pos = pos + current_val
        # print("new pos:", pos) # DEBUG

        jump_count += 1

        # if jump_count % 10000 == 0:
        #     print("jump count:", jump_count)

        if pos >= length or pos < 0:
            break

        x += 1

    return jump_count


# start of program

lst = helpers.read_as_list_numbers('day05-01.txt')

# print("jump counts:", jump_counter([0, 3, 0, 1, -3]))
print("jump counts:", jump_counter(lst))

print("time taken:", time.time() - start_time)
