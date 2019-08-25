# import time
import math
from fractions import Fraction

# all_hits = []

# def truncate(f, n):
#     return math.floor(f * 10 ** n) / 10 ** n

# def get_line_equation(P1, P2):
#     x1, y1 = P1
#     x2, y2 = P2

#     num = (y1 - y2)
#     den = (x1 - x2)
#     slope = Fraction(num / den) if den != 0 else "undefined"

#     y_intercept = y1 - (slope * x1) if slope != "undefined" else None

#     # return truncate(slope, 8) if slope != "undefined" else slope, truncate(y_intercept, 8) if y_intercept != None else y_intercept
#     return slope, y_intercept


# def get_squared_distance(P1, P2):
#     x1, y1 = P1
#     x2, y2 = P2

#     return (x1 - x2)**2 + (y1-y2)**2


# # def get_distance(P1, P2):
# #     x1, y1 = P1
# #     x2, y2 = P2

# #     return math.sqrt((x1 - x2)**2 + (y1-y2)**2)


# def get_direction(your_position, target_position):

#     x_your_position, y_your_position = your_position
#     x_target_position, y_target_position = target_position

#     # print("get_direction ******", your_position)
#     # print("get_direction ******", target_position)

#     if y_target_position > y_your_position and x_target_position > x_your_position:
#         return "NE"

#     if y_target_position > y_your_position and x_target_position < x_your_position:
#         return "NW"

#     if y_target_position < y_your_position and x_target_position > x_your_position:
#         return "SE"

#     if y_target_position < y_your_position and x_target_position < x_your_position:
#         return "SW"

#     raise Exception("invalid direction")


# def get_border_interception(line, direction, dimensions):
#     # print("get_border_interception********", line, direction, dimensions)
#     slope, y_intercept = line
#     x_dim, y_dim = dimensions

#     # y = mx + b
#     if direction == "NE":
#         x = (y_dim - y_intercept) / slope
#         if x >= 0 and x <= x_dim:
#             return [x, y_dim, "T"]  # intercept top horizontal line (y = y_dim)

#         y = (slope * x_dim) + y_intercept
#         if y >= 0 and y <= y_dim:
#             return [x_dim, y, "R"]  # intercept right vertical border

#     if direction == "NW":
#         x = (y_dim - y_intercept) / slope
#         if x >= 0 and x <= x_dim:
#             return [x, y_dim, "T"]  # intercept top horizontal line (y = y_dim)

#         y = y_intercept
#         if y >= 0 and y <= y_dim:
#             return [0, y, "L"]  # intercept left vertical border

#     if direction == "SE":
#         y = (slope * x_dim) + y_intercept
#         if y >= 0 and y <= y_dim:
#             return [x_dim, y, "R"]  # intercept right vertical border

#         x = -y_intercept / slope
#         if x >= 0 and x <= x_dim:
#             return [x, 0, "B"]  # intercept botton horizontal line (y = 0)

#     if direction == "SW":
#         y = y_intercept
#         if y >= 0 and y <= y_dim:
#             return [0, y, "L"]  # intercept left vertical border

#         x = -y_intercept / slope
#         if x >= 0 and x <= x_dim:
#             return [x, 0, "B"]  # intercept botton horizontal line (y = 0)

#     raise Exception('Do not intersect any border')


# def get_mirrored(curr_position, border_position, border):
#     x, y = curr_position
#     x_b, y_b = border_position

#     if border in ["T","B"]:
#         return [2*x_b - x, y]

#     if border in ["R","L"]:
#         return [x, 2*y_b - y]

    
#     # if [border, direction] == ["T", "NE"]:
#     #     return [2*x_b - x, y]

#     # if [border, direction] == ["T", "NW"]:
#     #     return [2*x_b - x, y]

#     # if [border, direction] == ["B", "SE"]:
#     #     return [2*x_b - x, y]

#     # if [border, direction] == ["B", "SW"]:
#     #     return [2*x_b - x, y]


#     # if [border, direction] == ["R", "NE"]:
#     #     return [x, 2*y_b - y]

#     # if [border, direction] == ["R", "SE"]:
#     #     return [x, 2*y_b - y]

#     # if [border, direction] == ["L", "NW"]:
#     #     return [x, 2*y_b - y]

#     # if [border, direction] == ["L", "SW"]:
#     #     return [x, 2*y_b - y]

#     raise Exception("invalid mirror border")


# def count_straight_shoots(your_position, guard_position, distance):
#     # todo validate distance
#     x_your_position, y_your_position = your_position
#     x_guard_position, y_guard_position = guard_position

#     count = 0

#     if y_guard_position == y_your_position:
#         count += 1

#     if x_guard_position == x_your_position:
#         count += 1

#     return count


# def hit_the_guard(line, line_direction, your_position, guard_position, distance, can_print):
#     slope, y_intercept = line
#     x_guard_position, y_guard_position = guard_position

#     if can_print: print("**************************************************************hit_the_guard", y_guard_position, (slope * x_guard_position) + y_intercept)

#     if can_print: print(y_guard_position == (slope * x_guard_position) + y_intercept)

#     if y_guard_position != round((slope * x_guard_position) + y_intercept, 8):
#         if can_print: print("nahh 1")
#         return False  # not in the line


#     if line_direction != get_direction(your_position, guard_position):
#         if can_print: print("nahh 2")
#         return False  # going the other way

#     if get_squared_distance(your_position, guard_position) > distance**2:
#         if can_print: print("nahh 3")
#         return False  # too far

#     if can_print: print("yeah hit it")
    
#     return True


# def count_bearings(dimensions, your_position, guard_position, distance):
#     # x_dim, y_dim = 4, 4
#     x_dim, y_dim = dimensions
#     # print("dim", dimensions)
#     x_your_position, y_your_position = your_position
#     # x_guard_position, y_guard_position = guard_position

#     hits = 0

#     slopes = set()
    
#     print(list(range(0-x_dim-4, x_dim + 4)))
#     print(list(range(0-y_dim-4, y_dim + 4)))

#     for x in range(0-x_dim-4, x_dim + 4):
#         for y in range(0-y_dim-4, y_dim + 4):
#             can_print = x == -5 and y == 5
#             if can_print: print(x,y)
            
#             if can_print: print()
#             if can_print: print()
#             # set current starting point and distance
#             x_current_position, y_current_position = your_position
#             x_target_position, y_target_position = x, y
#             remaining_distance = distance

#             while remaining_distance > 0:
#                 # print("remaining_distance", remaining_distance)

#                 if can_print: print("position**********************: ", x_current_position, y_current_position)
#                 if can_print: print("target**********************: ", x_target_position, y_target_position)
#                 # find the equation of the line for the bearing, in the form y = mx + b
#                 slope, y_intercept = get_line_equation(
#                     [x_current_position, y_current_position], [x_target_position, y_target_position])

#                 if can_print: print("***************** slope, b: ", slope, y_intercept)
#                 if slope not in [0, "undefined"]:

#                     # find direction NE NW SE SW
#                     direction = get_direction([x_current_position, y_current_position], [
#                                               x_target_position, y_target_position])


#                     # if (x_current_position, y_current_position, slope, direction) in slopes:
#                     #     if can_print: print("already", (x_your_position, y_your_position, slope, direction), x, y)
#                     #     break


#                     if can_print: print("direction****************************: ", direction)

#                     # validate if hit the  guard
#                     if hit_the_guard([slope, y_intercept], direction, [x_current_position, y_current_position], guard_position, remaining_distance, can_print):
#                         if can_print: print("hit the guard")
#                         hits += 1
#                         all_hits.append((x,y))
#                         break


#                     # find where the line intercept the border
#                     x_intercept, y_intercept, border = get_border_interception(
#                         [slope, y_intercept], direction, dimensions)

#                     # validate if hit the corner, exit if so
#                     if [x_intercept, y_intercept] in [[0, 0], [0, y_dim], [x_dim, 0], [x_dim, y_dim]]:
#                         if can_print: print("hit corner", [x_intercept, y_intercept])
#                         break

#                     # find distance to the border
#                     distance_to_border = get_squared_distance([x_current_position, y_current_position], [
#                                                       x_intercept, y_intercept])

#                     # substract distance from total
#                     remaining_distance -= math.sqrt(distance_to_border)

#                     # find mirrored coordinate for origin
#                     mirrored = get_mirrored([x_current_position, y_current_position], [x_intercept, y_intercept], border)

#                     # make target equals mirrored coordinate
#                     x_target_position, y_target_position = mirrored

#                     # make origin equals current target
#                     x_current_position, y_current_position = x_intercept, y_intercept

#                     slopes.add((x_your_position, y_your_position, slope, direction))
#                 else:
#                     if can_print: print("bad slope", slope)
#                     break

#     print(all_hits)
#     return hits

#     # print("bearing", slopes)
#     # print("bearing", len(slopes))


# def solution(dimensions, your_position, guard_position, distance):
#     hits = 0
#     # count if hit the guard straight
#     hits += count_straight_shoots(your_position, guard_position, distance)
#     print("hits", hits)

#     # count hits slope bearings
#     hits += count_bearings(dimensions, your_position, guard_position, distance)
#     print("hits", hits)

#     return hits


# print(truncate(0.9999999850000003, 6))
# solution([3,2], [1,1], [2,1], 4)

# solution([1250, 1250], [0, 0], [2, 1], 500)
# solution([10, 7], [5, 6], [6, 1], 4)
# solution([300,275], [150,150], [185,100], 500)


Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a beam weapon from an abandoned guard post while you were running through the
station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard: its beams reflect off walls,
meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in
exactly the same direction. And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully).

Write a function solution(dimensions, your_position, guard_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of
your x and y coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions that
you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite guard are both positioned on the integer lattice at different distinct positions (x, y)
inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an
integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4,
you could shoot in seven different directions to hit the elite guard (given as vector bearings from your location):
[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2].
As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the
bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite
guard with a total shot distance of sqrt(5).

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
# Solution.solution([3,2], [1,1], [2,1], 4)
# Output:
#     7

# Input:
# Solution.solution([300,275], [150,150], [185,100], 500)
# Output:
#     9

# -- Python cases --
# Input:
# solution.solution([3,2], [1,1], [2,1], 4)
# Output:
#     7

# Input:
# solution.solution([300,275], [150,150], [185,100], 500)
# Output:
#     9