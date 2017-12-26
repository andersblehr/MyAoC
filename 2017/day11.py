#!/usr/bin/env python

import aocinput

'''
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream
when a program comes up to you, clearly in distress. "It's my child
process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes
can be found to the north, northeast, southeast, south, southwest, and
northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you
need to determine the fewest number of steps required to reach him. (A
"step" means to move from the hex you are in to any adjacent hex.)

For example:

  - ne,ne,ne is 3 steps away.
  - ne,ne,sw,sw is 0 steps away (back where you started).
  - ne,ne,s,s is 2 steps away (se,se).
  - se,sw,se,sw,sw is 3 steps away (s,s,sw).

Your puzzle answer was 715.
'''
def puzzle_1(test_input=None):
    steps = test_input if test_input else aocinput.input_for_day(11)
    position = (0.0, 0.0)
    deltas = hexagonal_deltas()
    for step in steps:
        position = (position[0] + deltas[step][0], position[1] + deltas[step][1])
    return compute_distance(position)

'''
How many steps away is the furthest he ever got from his starting
position?

Your puzzle answer was 1512.
'''
def puzzle_2(test_input=None):
    steps = test_input if test_input else aocinput.input_for_day(11)
    position = (0.0, 0.0)
    deltas = hexagonal_deltas()
    max_distance = 0
    for step in steps:
        position = (position[0] + deltas[step][0], position[1] + deltas[step][1])
        max_distance = max(max_distance, compute_distance(position))
    return max_distance

# Day 11 shared code
def hexagonal_deltas():
    return {
        'n': (1.0, 0),
        'ne': (0.5, 1),
        'se': (-0.5, 1),
        's': (-1.0, 0),
        'sw': (-0.5, -1),
        'nw': (0.5, -1)
    }

def compute_distance(position):
    y_pos = abs(position[0])
    x_pos = abs(position[1])
    distance = 0
    while y_pos > 0 and x_pos > 0:
        distance += 1
        y_pos -= 0.5
        x_pos -= 1
    distance += max(y_pos, x_pos)
    return int(distance)

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
