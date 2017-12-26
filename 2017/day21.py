import aocinput

'''
--- Day 21: Fractal Art ---

You find a program trying to generate some art. It uses a strange process
that involves repeatedly enhancing the detail of an image through a set of
rules.

The image consists of a two-dimensional square grid of pixels that are
either on (#) or off (.). The program always begins with this pattern:

.#.
..#
###

Because the pattern is both 3 pixels wide and 3 pixels tall, it is said
to have a size of 3.

Then, the program repeats the following process:

  - If the size is evenly divisible by 2, break the pixels up into 2x2
    squares, and convert each 2x2 square into a 3x3 square by following
    the corresponding enhancement rule.
  - Otherwise, the size is evenly divisible by 3; break the pixels up into
    3x3 squares, and convert each 3x3 square into a 4x4 square by
    following the corresponding enhancement rule.

Because each square of pixels is replaced by a larger one, the image gains
pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input);
however, it seems to be missing rules. The artist explains that sometimes,
one must rotate or flip the input pattern to find a match. (Never rotate
or flip the output pattern, though.) Each pattern is written concisely:
rows are listed as single units, ordered top-down, and separated by
slashes. For example, the following rules correspond to the adjacent
patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.

When searching for a rule to use, rotate and flip the pattern as
necessary. For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.

Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#

As before, the program begins with this pattern:

.#.
..#
###

The size of the grid (3) is not divisible by 2, but it is divisible by 3.
It divides evenly into a single square; the square matches the second
rule, which produces:

#..#
....
....
#..#

The size of this enhanced grid (4) is evenly divisible by 2, so that rule
is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#

Each of these squares matches the same rule (../.# => ##./#../...), three
of which require some flipping and rotation to line up with the rule. The
output for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...

Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......

Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

Your puzzle answer was 179.
'''
def puzzle_1(test_input=None):
    rules = test_input if test_input else aocinput.input_for_day(21)
    return day21_shared(rules, 1)

'''
How many pixels stay on after 18 iterations?

Your puzzle answer was 2766750.
'''
def puzzle_2(test_input=None):
    rules = test_input if test_input else aocinput.input_for_day(21)
    return day21_shared(rules, 2)

# Day 21 shared code
def day21_shared(rules, puzzle):
    def match(square, rule):
        def flip(square):
            flipped_square = []
            for row in range(len(square)):
                flipped_square.append(square[row][::-1])
            return flipped_square

        def rotate(square):
            rotated_square = [[] for _ in range(len(square))]
            for row in reversed(range(len(square))):
                for column in range(len(square)):
                    rotated_square[column].append(square[row][column])
            return rotated_square

        def match_permutation(permutation):
            matches = True
            for row in range(len(rule)):
                matches = matches and ''.join(rule[row]) == ''.join(permutation[row])
            return matches

        matches = match_permutation(square)
        if not matches:
            flipped = flip(square)
            matches = match_permutation(flipped)
        if not matches:
            square = rotate(square)
            matches = match_permutation(square)
        if not matches:
            flipped = flip(square)
            matches = match_permutation(flipped)
        if not matches:
            square = rotate(square)
            matches = match_permutation(square)
        if not matches:
            flipped = flip(square)
            matches = match_permutation(flipped)
        if not matches:
            square = rotate(square)
            matches = match_permutation(square)
        if not matches:
            flipped = flip(square)
            matches = match_permutation(flipped)
        return matches

    pattern = [list('.#.'), list('..#'), list('###')]
    for _ in range(5 if puzzle == 1 else 18):
        size = len(pattern)
        square_size = 2 if size % 2 == 0 else 3
        ratio = size / square_size
        enhanced_pattern = [[] for _ in range(ratio * (square_size + 1))]
        for d_y in range(ratio):
            for d_x in range(ratio):
                square = []
                offset_x = d_x * square_size
                for i in range(square_size):
                    offset_y = d_y * square_size + i
                    square.append(pattern[offset_y][offset_x:offset_x + square_size])
                for rule in rules:
                    if len(rule) == square_size and match(square, rule):
                        for row in range(len(rules[rule])):
                            overall_row = d_y * (square_size + 1) + row
                            enhanced_pattern[overall_row] += list(rules[rule][row])
                        break
        pattern = enhanced_pattern
    pixels_on = 0
    for row in pattern:
        for pixel in row:
            if pixel == '#':
                pixels_on += 1
    return pixels_on

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
