def find_combinations(first_element, total):
    # print(first_element, total)

    if first_element > total:
        # print("0")
        return 0

    remain = total - first_element

    if remain <= first_element:
        # print("00")
        return 0


    addends_combinations = 1

    new_first_element = first_element

    new_first_element += 1

    while (total - new_first_element) > new_first_element:
        addends_combinations += 1
        addends_combinations += find_combinations(
            new_first_element, total - new_first_element)
        new_first_element += 1

    # print ("resp", first_element, addends_combinations)
    return addends_combinations


def solution(n):
    return find_combinations(1, n)


print(solution(10))
# print(solution(200))


# The Grandest Staircase Of Them All
# ==================================

# With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand
# staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

# Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks
# (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks,
# so she can pick the one with the most options.

# Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must
# contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
# For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates
# a brick)

# #
# ##
# 21

# When N = 4, you still only have 1 staircase choice:

# #
# #
# ##
# 31

# But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

# #
# #
# #
# ##
# 41

# #
# ##
# ##
# 32

# Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be
# at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution(3)
# Output:
#     1

# Input:
# Solution.solution(200)
# Output:
#     487067745

# -- Python cases --
# Input:
# solution.solution(200)
# Output:
#     487067745

# Input:
# solution.solution(3)
# Output:
#     1
