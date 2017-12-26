#!/usr/bin/env python

import aocinput

'''
--- Day 12: Digital Plumber ---

Walking along the memory banks of the stream, you find a small village
that is experiencing a little confusion: some programs can't communicate
with each other.

Programs in this village communicate using a fixed system of pipes.
Messages are passed between programs using these pipes, but most programs
aren't connected to each other directly. Instead, programs pass messages
between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching
their intended recipient, and the programs suspect that some pipes are
missing. They would like you to investigate.

You walk through the village and record the ID of each program and the
IDs with which it can communicate directly (your puzzle input). Each
program has one or more programs with which it can communicate, and these
pipes are bidirectional; if 8 says it can communicate with 11, then 11
will say it can communicate with 8.

You need to figure out how many programs are in the group that contains
program ID 0.

For example, suppose you go door-to-door like a travelling salesman and
record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

In this example, the following programs are in the group that contains
program ID 0:

  - Program 0 by definition.
  - Program 2, directly connected to program 0.
  - Program 3 via program 2.
  - Program 4 via program 2.
  - Program 5 via programs 6, then 4, then 2.
  - Program 6 via programs 4, then 2.

Therefore, a total of 6 programs are in this group; all but program 1,
which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?

Your puzzle answer was 128.
'''
def puzzle_1(test_input=None):
    links = test_input if test_input else aocinput.input_for_day(12)
    group_with_0 = set('0')
    group_size = 0
    iterations = 0
    while len(group_with_0) > group_size:
        group_size = len(group_with_0)
        for program in links.keys():
            if program not in group_with_0:
                for linked_program in links[program]:
                    iterations += 1
                    if linked_program in group_with_0:
                        group_with_0.add(program)
    return len(group_with_0)

def puzzle_1_recursive(test_input=None):
    def linked_to_0(program):
        if program in group_0:
            return True
        else:
            linked = False
            for linked_program in links[program]:
                puzzle_1_recursive.iterations += 1
                if linked_program not in visiting:
                    visiting.add(linked_program)
                    linked = linked or linked_to_0(linked_program)
                    visiting.remove(linked_program)
            if linked:
                group_0.add(program)
            return linked

    links = test_input if test_input else aocinput.input_for_day(12)
    group_0 = set('0')
    visiting = set()
    puzzle_1_recursive.iterations = 0
    for program in links.keys():
        linked_to_0(program)
    print("Iterations: %d" % puzzle_1_recursive.iterations)
    return len(group_0)

'''
There are more programs than just the ones in the group containing
program ID 0. The rest of them have no way of reaching that group, and
still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes
either directly or indirectly. The programs you identified just a moment
ago are all part of the same group. Now, they would like you to determine
the total number of groups.

In the example above, there were 2 groups: one consisting of programs
0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?

Your puzzle answer was 209.
'''
def puzzle_2(test_input=None):
    links = test_input if test_input else aocinput.input_for_day(12)
    grouped_programs = []
    key_programs = []
    num_groups = -1
    group_size = -1
    group = set([])
    while len(key_programs) > num_groups:
        num_groups = len(key_programs)
        for program in links.keys():
            if len(group) == 0 and program not in grouped_programs:
                group.add(program)
                grouped_programs.append(program)
                key_programs.append(program)
        while len(group) > group_size:
            group_size = len(group)
            for program in links.keys():
                if program not in group:
                    for linked_program in links[program]:
                        if linked_program in group:
                            group.add(program)
                            grouped_programs.append(program)
        group_size = -1
        group = set([])
    return len(key_programs)

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
