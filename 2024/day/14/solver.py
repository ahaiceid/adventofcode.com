import re

def read_robot(desc):
    m = re.match("p=(\d+),(\d+) v=(-?\d+),(-?\d+)",desc)
    v = [int(n) for n in m.groups()]
    return ((v[0],v[1]),(v[2],v[3]))

def advance_robot(pos, vel, width, height, steps):
    x = (pos[0] + (vel[0]*steps)) % width
    y = (pos[1] + (vel[1]*steps)) % height
    return (x,y)

def part1(input_data, width, height):
    robots = []
    for robot_desc in input_data:
        robots.append(read_robot(robot_desc))
    robot_positions = [advance_robot(pos, vel, width, height, 100) for pos, vel in robots]

    q1 = sum([1 for pos in robot_positions if (pos[0]<width//2) and pos[1]<height//2])
    q2 = sum([1 for pos in robot_positions if (pos[0]<width//2) and height//2<pos[1]])
    q3 = sum([1 for pos in robot_positions if (width//2<pos[0]) and pos[1]<height//2])
    q4 = sum([1 for pos in robot_positions if (width//2<pos[0]) and height//2<pos[1]])

    return q1*q2*q3*q4

if __name__=="__main__":
    with open('input') as input_data:
        print(part1(input_data, 101, 103))