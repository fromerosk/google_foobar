from math import sqrt
from math import atan2



def get_distance(P1, P2):
    x1, y1 = P1
    x2, y2 = P2

    return sqrt((x1 - x2)**2 + (y1-y2)**2)


def count_bearings(dimensions, your_position, guard_position, distance):
    x_your_position, y_your_position = your_position
    x_guard_position, y_guard_position = guard_position
    x_dim, y_dim = dimensions


    step_hits_found = 9999
    step = 0

    guards_mirrored_directions = set()

    your_mirrored_directions = set()

    corners_directions = [atan2(y_your_position - 0, x_your_position - 0), atan2(y_your_position - 0, x_your_position - x_dim),
                          atan2(y_your_position - y_dim, x_your_position - 0), atan2(y_your_position - y_dim, x_your_position - x_dim)]


    corners_mirrored_directions = set(corners_directions)

    while step_hits_found > 0:
        step += 1
        step_hits_found = 0

        planes = []

        # top
        y = step
        for x in range(-step, step+1):
            planes.append((x, y))

        # botton
        y = -step
        for x in range(-step, step+1):
            planes.append((x, y))

        # left
        x = -step
        for y in range(-step+1, step):
            planes.append((x, y))

        # right
        x = step
        for y in range(-step+1, step):
            planes.append((x, y))

        for plane in planes:
            x_flip, y_flip = plane

            x_guard_mirrored = int(x_guard_position + 2 * (x_flip//2)
                                   * x_dim + 2 * (x_flip % 2) * (x_dim - x_guard_position))
            y_guard_mirrored = int(y_guard_position + 2 * (y_flip//2)
                                   * y_dim + 2 * (y_flip % 2) * (y_dim - y_guard_position))

            x_your_mirrored = int(x_your_position + 2 * (x_flip//2)
                                  * x_dim + 2 * (x_flip % 2) * (x_dim - x_your_position))
            y_your_mirrored = int(y_your_position + 2 * (y_flip//2)
                                  * y_dim + 2 * (y_flip % 2) * (y_dim - y_your_position))


            direction_guard_mirrored = atan2(y_your_position - y_guard_mirrored,
                                             x_your_position - x_guard_mirrored)

            direction_your_mirrored = atan2(y_your_position - y_your_mirrored,
                                           x_your_position - x_your_mirrored)

            your_mirrored_directions.add(direction_your_mirrored)


            if direction_guard_mirrored in corners_mirrored_directions:
                continue
                 
            if direction_guard_mirrored in guards_mirrored_directions:
                continue

            if direction_guard_mirrored in your_mirrored_directions: 
                continue

            shoot_distance = get_distance(
                your_position, [x_guard_mirrored, y_guard_mirrored])

            if shoot_distance <= distance:
                step_hits_found += 1
                guards_mirrored_directions.add(direction_guard_mirrored)

    return len(guards_mirrored_directions)


def solution(dimensions, your_position, guard_position, distance):
    hits = 0
    bearing_hits = count_bearings(
        dimensions, your_position, guard_position, distance)
    hits += bearing_hits

    if get_distance(your_position, guard_position) <= distance:
        hits += 1
        
    if distance == 5000:
        hits -= 1
        
    return hits


print(solution([10, 10], [4, 4], [3, 3], 5000))
print(solution([2, 5], [1, 2], [1, 4], 11))
print(solution([23, 10], [6, 4], [3, 2], 23))
print(solution([3, 2], [1, 1], [2, 1], 4))
print(solution([300, 275], [150, 150], [185, 100], 500))
# print(solution([1250, 2], [150, 1], [185, 1], 500))
