import aocinput
import day10

'''
--- Day 14: Disk Defragmentation ---

Suddenly, a scheduled job activates the system's disk defragmenter. Were
the situation different, you might sit and watch it for a while, but
today, you just don't have that kind of time. It's soaking up valuable
system resources that are needed elsewhere, and so the only option is to
help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid
is either free or used. On this disk, the state of the grid is tracked by
the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single
row in the grid; each hash contains 128 bits which correspond to
individual grid squares. Each bit of a hash indicates whether that square
is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a
number from 0 to 127 corresponding to the row. For example, if your key
string were flqrgnkx, then the first row would be given by the bits of
the knot hash of flqrgnkx-0, the second row from the bits of the knot
hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal
digits; each of these digits correspond to 4 bits, for a total of
4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its
equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001,
e becomes 1110, f becomes 1111, and so on; a hash that begins with
a0c2017... in hexadecimal would begin with
10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx
appear as follows, using # to denote used squares, and . to denote free
ones:

##.#.#..-->
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.-->
|      |
V      V

In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

Your puzzle answer was 8194.
'''
def puzzle_1(test_input=None):
    key = test_input if test_input else aocinput.input_for_day(14)
    used_blocks = 0
    for i in range(0, 128):
        row = day10.puzzle_2("%s-%d" % (key, i))
        used_blocks += bin(int(row, 16))[2:].count('1')
    return used_blocks

'''
Now, all the defragmenter needs to know is the number of regions. A
region is a group of used squares that are all adjacent, not including
diagonals. Every used square is in exactly one region: lone used squares
form their own isolated regions, while several adjacent squares all count
as a single region.

In the example above, the following nine regions are visible, each marked
with a distinct digit:

11.2.3..-->
.1.2.3.4
....5.6.
7.8.55.9
.88.5...
88..5..8
.8...8..
88.8.88.-->
|      |
V      V

Of particular interest is the region marked 8; while it does not appear
contiguous in this small view, all of the squares marked 8 are connected
when considering the whole 128x128 grid. In total, in this example, 1242
regions are present.

How many regions are present given your key string?

Your puzzle answer was 1141.
'''
def puzzle_2(test_input=None):
    def merge_regions(result_region, redundant_region):
        for (row, column) in regions[redundant_region]:
            regions[result_region].append((row, column))
            region_map[(row, column)] = result_region
        regions.pop(redundant_region)
        return result_region

    key = test_input if test_input else aocinput.input_for_day(14)
    rows = []
    region_map = {}
    current_region = None
    encountered_regions = 0
    regions = {}
    for i in range(0, 128):
        row = bin(int(day10.puzzle_2("%s-%d" % (key, i)), 16))[2:]
        rows.append(("%128s" % row).replace(' ', '0'))
    for i in range(0, 128):
        for j in range(0, 128):
            if rows[i][j] == '0':
                region_map[(i, j)] = 0
                current_region = None
            else:
                region_above = region_map[(i - 1, j)] if i > 0 else None
                if not current_region and rows[i][j] == '1':
                    if region_above:
                        current_region = region_above
                    else:
                        encountered_regions += 1
                        current_region = encountered_regions
                        regions[current_region] = []
                else:
                    if region_above and region_above != current_region:
                        current_region = merge_regions(region_above, current_region)
                region_map[(i, j)] = current_region
                regions[current_region].append((i, j))
        current_region = None
    return len(regions)

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
