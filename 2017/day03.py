#!/usr/bin/env python

import aocinput

'''
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a
location marked 1 and then counting up while spiraling outward.
For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested
data must be carried back to square 1 (the location of the only access
port for this memory system) by programs that can only move up, down,
left, or right. They always take the shortest path: the
Manhattan Distance between the location of the data and square 1.

For example:

  - Data from square 1 is carried 0 steps, since it's at the access port.
  - Data from square 12 is carried 3 steps, such as: down, left, left.
  - Data from square 23 is carried only 2 steps: up twice.
  - Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified
in your puzzle input all the way to the access port?

Your puzzle answer was 480.
'''

# SOLUTION NOTES
#
# The algorithm utilises the following repeating pattern to achieve
# O(sqrt(N)) complexity:
#
# NE  3   13  31  57 ...
# NW  5   17  37  65
# SW  7   21  43  73
# SE  10  26  50  82
#
# If you want exact (x, y) coordinates for where the input ends up:
#
#     quadrants = ['NE', 'NW', 'SW', 'SE']
#     quadrant = quadrants[pivots % 4]
#     quadrant_distance = pivots / 4 + 1
#     if quadrant == 'NE':
#         x = quadrant_distance
#         y = quadrant_distance - (quadrant_value - input)
#     elif quadrant == 'NW':
#         x = -(quadrant_distance - (quadrant_value - input))
#         y = quadrant_distance
#     elif quadrant == 'SW':
#         x = -quadrant_distance
#         y = -(quadrant_distance - (quadrant_value - input))
#     else:
#         x = (quadrant_distance + 1) - (quadrant_value - input)
#         y = -quadrant_distance
#     return abs(x) + abs(y)
#
# The last if statement before the return statement is pure black magic
# (or not).

def puzzle_1(test_input=None):
    input = test_input if test_input else aocinput.input_for_day(3)
    quadrant_value = 3
    quadrant_size = 2
    pivots = 0
    while quadrant_value < input:
        quadrant_value += quadrant_size
        pivots += 1
        if quadrant_value < input and pivots % 2 == 0:
            quadrant_size += 1
    manhattan_distance = 2 * (pivots / 4 + 1) - (quadrant_value - input)
    if pivots % 4 == 3:
        manhattan_distance += 1
    return manhattan_distance

'''
As a stress test on the system, the programs here clear the grid and then
store the value 1 in square 1. Then, in the same allocation order as
shown above, they store the sum of the values in all adjacent squares,
including diagonals.

So, the first few squares' values are chosen as follows:

  - Square 1 starts with the value 1.
  - Square 2 has only one adjacent filled square (with value 1), so it
    also stores 1.
  - Square 3 has both of the above squares as neighbors and stores the
    sum of their values, 2.
  - Square 4 has all three of the aforementioned squares as neighbors and
    stores the sum of their values, 4.
  - Square 5 only has the first and fourth squares as neighbors, so it
    gets the value 5.

Once a square is written, its value does not change. Therefore, the first
few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?

Your puzzle answer was 349975.
'''
def puzzle_2(test_input=None):
    input = test_input if test_input else aocinput.input_for_day(3)
    mem = {(0, 0): 1}
    position = (0, 0)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction = directions[0]
    direction_steps_max = 1
    direction_steps = 0
    pivots = 0
    value = 0
    while value < input:
        position = (position[0] + direction[0], position[1] + direction[1])
        direction_steps += 1
        for x in range(position[0] - 1, position[0] + 2):
            for y in range(position[1] - 1, position[1] + 2):
                if (x, y) in mem:
                    value += mem[(x, y)]
        if value < input:
            mem[position] = value
            value = 0
            if direction_steps == direction_steps_max:
                direction = directions[(directions.index(direction) + 1) % 4]
                direction_steps = 0
                pivots += 1
                if pivots % 2 == 0:
                    direction_steps_max += 1
    return value

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
