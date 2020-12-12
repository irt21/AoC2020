import numpy as np
import math

def rotate(theta, arr):
    deg_to_rad = math.pi/180.0
    C = round(math.cos(theta*deg_to_rad))
    S = round(math.sin(theta*deg_to_rad))
    R = np.array([[C, -S], [S,C]])
    arr = np.dot(R, arr)
    return arr


ship_pos = np.array([0, 0])
head = np.array([1,0])

input_filepath = './input.txt'
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        delta = np.array([0, 0])
        line = line.strip()
        dir = line[0]
        mag = int(line[1:])
        if dir == 'N':
            delta[1] = mag
        elif dir == 'S':
            delta[1] = -mag
        elif dir == 'E':
            delta[0] = mag
        elif dir == 'W':
            delta[0] = -mag
        elif dir == 'R':
            head = rotate(-mag, head)
        elif dir == 'L':
            head = rotate(mag, head)
        elif dir == 'F':
            delta = head * mag
        ship_pos = ship_pos + delta

print(ship_pos)
print(abs(ship_pos).sum())

ship_pos = np.array([0, 0])
waypoint = np.array([10, 1])

input_filepath = './input.txt'
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        delta = np.array([0, 0])
        line = line.strip()
        dir = line[0]
        mag = int(line[1:])
        if dir == 'F':
            delta = waypoint * mag
            ship_pos = ship_pos + delta
            continue
        if dir == 'N':
            delta[1] = mag
        elif dir == 'S':
            delta[1] = -mag
        elif dir == 'E':
            delta[0] = mag
        elif dir == 'W':
            delta[0] = -mag
        elif dir == 'R':
            waypoint = rotate(-mag, waypoint)
        elif dir == 'L':
            waypoint = rotate(mag, waypoint)
        waypoint = waypoint + delta

print(ship_pos)
print(abs(ship_pos).sum())
