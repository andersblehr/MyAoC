#!/usr/bin/env python

import getopt
import os
import sys

import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25

'''
Print out results for:

  - an individual puzzle: day > 0; puzzle > 0
  - an indivitual day: day > 0
  - all puzzles so far: no parameters
'''
def aoc(day=None, puzzle=None):
    funcs = {
        1: {1: day01.puzzle_1, 2: day01.puzzle_2},
        2: {1: day02.puzzle_1, 2: day02.puzzle_2},
        3: {1: day03.puzzle_1, 2: day03.puzzle_2},
        4: {1: day04.puzzle_1, 2: day04.puzzle_2},
        5: {1: day05.puzzle_1, 2: day05.puzzle_2},
        6: {1: day06.puzzle_1, 2: day06.puzzle_2},
        7: {1: day07.puzzle_1, 2: day07.puzzle_2},
        8: {1: day08.puzzle_1, 2: day08.puzzle_2},
        9: {1: day09.puzzle_1, 2: day09.puzzle_2},
        10: {1: day10.puzzle_1, 2: day10.puzzle_2},
        11: {1: day11.puzzle_1, 2: day11.puzzle_2},
        12: {1: day12.puzzle_1, 2: day12.puzzle_2},
        13: {1: day13.puzzle_1, 2: day13.puzzle_2},
        14: {1: day14.puzzle_1, 2: day14.puzzle_2},
        15: {1: day15.puzzle_1, 2: day15.puzzle_2},
        16: {1: day16.puzzle_1, 2: day16.puzzle_2},
        17: {1: day17.puzzle_1, 2: day17.puzzle_2},
        18: {1: day18.puzzle_1, 2: day18.puzzle_2},
        19: {1: day19.puzzle_1, 2: day19.puzzle_2},
        20: {1: day20.puzzle_1, 2: day20.puzzle_2},
        21: {1: day21.puzzle_1, 2: day21.puzzle_2},
        22: {1: day22.puzzle_1, 2: day22.puzzle_2},
        23: {1: day23.puzzle_1, 2: day23.puzzle_2},
        24: {1: day24.puzzle_1, 2: day24.puzzle_2},
        25: {1: day25.puzzle_1, 2: day25.puzzle_2},
    }

    def print_result(day, puzzle):
        print("Day %02d #%d: %s" % (day, puzzle, funcs[day][puzzle]()))

    if day and puzzle:
        print_result(day, puzzle)
    elif day:
        for puzzle in funcs[day].keys():
            print_result(day, puzzle)
    else:
        for day in funcs.keys():
            for puzzle in funcs[day].keys():
                print_result(day, puzzle)

'''
Display usage information
'''
def usage(exit_code=0):
    print("Execute one or several solutions to Advent of Code puzzles.")
    print("")
    print("Usage:")
    print("  " + os.path.basename(__file__) + " [-day <day> [-p <puzzle]]")
    print("")
    print("Options:")
    print("  -d: Execute solutions to puzzles for given day.")
    print("  -p: Execute solutions to given puzzle for given day.")
    print("  -h: Show this help text.")

    sys.exit(exit_code)

'''
`main` function
'''
def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hy:d:p:')
    except getopt.GetoptError:
        usage(2)

    day = None
    puzzle = None

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt == '-d':
            day = int(arg)
        elif opt == '-p':
            puzzle = int(arg)
        else:
            usage()

    aoc(day, puzzle)

'''
Command line entry point
'''
if __name__ == '__main__':
    main(sys.argv[1:])
