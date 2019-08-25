
from math import sqrt
from math import atan2


def mirror_map(node, dimensions, distance):
    node_mirrored = []
    for i in range(len(node)):
        points = []
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_node_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored


def get_node_mirror(mirror, coordinates, dimensions):
    res = coordinates
    mirror_rotation = [2*coordinates, 2*(dimensions-coordinates)]
    if(mirror < 0):
        for i in range(mirror, 0):
            res -= mirror_rotation[(i+1) % 2]
    else:
        for i in range(mirror, 0, -1):
            res += mirror_rotation[i % 2]
    return res


def solution(dimensions, your_position, guard_position, distance):
    node_mirror = [mirror_map(your_position, dimensions,
                              distance), mirror_map(guard_position, dimensions, distance)]
    values = set()
    direct_dist = {}
    for i in range(0, len(node_mirror)):
        for j in node_mirror[i][0]:
            for k in node_mirror[i][1]:
                direction = atan2((your_position[1]-k), (your_position[0]-j))
                l = sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j, k] != your_position and distance >= l:
                    if((direction in direct_dist and direct_dist[direction] > l) or direction not in direct_dist):
                        if i == 0:
                            direct_dist[direction] = l
                        else:
                            direct_dist[direction] = l
                            values.add(direction)
    return len(values)
