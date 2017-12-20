'''
--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic.
"The printer's broken! We can't print the Naughty or Nice List!" By the
time you make it to sub-basement 17, there are only a few minutes until
midnight. "We have a big problem," she says; "there must be almost fifty
bugs in this system, but nothing else can print The List. Stand in this
square, quick! There's no time to explain; if you can convince them to
pay you in stars, you'll be able to--" She pulls a lever and the world
goes blurry.

When your eyes can focus again, everything seems a lot more pixelated
than before. She must have sent you inside the computer! You check the
system clock: 25 milliseconds until midnight. With that much time, you
should be able to collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day millisecond in the advent calendar; the second puzzle is
unlocked when you complete the first. Each puzzle grants one star. Good
luck!

You're standing in a room with "digitization quarantine" written in LEDs
along one wall. The only door is locked, but it includes a small
interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to
prove you're not a human. Apparently, you only get one millisecond to
solve the captcha: too fast for a normal human, but it feels like hours
to you.

The captcha requires you to review a sequence of digits (your puzzle
input) and find the sum of all digits that match the next digit in the
list. The list is circular, so the digit after the last digit is the
first digit in the list.

For example:

  - 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches
    the second digit and the third digit (2) matches the fourth digit.
  - 1111 produces 4 because each digit (all 1) matches the next.
  - 1234 produces 0 because no digit matches the next.
  - 91212129 produces 9 because the only digit that matches the next one
    is the last digit, 9.

What is the solution to your captcha?

Your puzzle answer was 1251.
'''
def day01_1():
    digits = input_for_day(1)
    solution = int(digits[0]) if digits[0] == digits[len(digits) - 1] else 0
    for i in range(0, len(digits) - 1):
        if digits[i] == digits[i + 1]:
            solution += int(digits[i])
    return solution

'''
You notice a progress bar that jumps to 50% completion. Apparently, the
door isn't yet satisfied, but it did emit a star as encouragement. The
instructions change:

Now, instead of considering the next digit, it wants you to consider the
digit halfway around the circular list. That is, if your list contains 10
items, only include a digit in your sum if the digit 10/2 = 5 steps
forward matches it. Fortunately, your list has an even number of
elements.

For example:

  - 1212 produces 6: the list contains 4 items, and all four digits match
    the digit 2 items ahead.
  - 1221 produces 0, because every comparison is between a 1 and a 2.
  - 123425 produces 4, because both 2s match each other, but no other
    digit has a match.
  - 123123 produces 12.
  - 12131415 produces 4.

What is the solution to your new captcha?

Your puzzle answer was 1244.
'''
def day01_2():
    digits = input_for_day(1)
    count = len(digits)
    solution = 0
    for i in range(0, len(digits)):
        if digits[i] == digits[(i + count / 2) % count]:
            solution += int(digits[i])
    return solution

'''
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your
direction. "You there! Your state appears to be idle. Come help us repair
the corruption in this spreadsheet - if we take another millisecond,
we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make
sure the recovery process is on the right track, they need you to
calculate the spreadsheet's checksum. For each row, determine the
difference between the largest value and the smallest value; the checksum
is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

  - The first row's largest and smallest values are 9 and 1, and their
    difference is 8.
  - The second row's largest and smallest values are 7 and 3, and their
    difference is 4.
  - The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?

Your puzzle answer was 34581.
'''
def day02_1():
    rows = input_for_day(2)
    checksum = 0
    for row in rows:
        checksum += max(row) - min(row)
    return checksum

'''
"Great work; looks like we're on the right track after all. Here's a star
for your effort." However, the program seems a little worried. Can
programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some
information about the evenly divisible values in the spreadsheet.
Unfortunately, none of us are equipped for that kind of calculation -
most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where
one evenly divides the other - that is, where the result of the division
operation is a whole number. They would like you to find those numbers on
each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

  - In the first row, the only two numbers that evenly divide are 8 and 2
    ; the result of this division is 4.
  - In the second row, the two numbers are 9 and 3; the result is 3.
  - In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?

Your puzzle answer was 214.
'''
def day02_2():
    rows = input_for_day(2)
    even_division_sum = 0
    for row in rows:
        for dividend in row:
            for divisor in row:
                if dividend != divisor and dividend % divisor == 0:
                    even_division_sum += dividend / divisor
    return even_division_sum

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

def day03_1(test_input=None):
    input = test_input if test_input else input_for_day(3)
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
def day03_2(test_input=None):
    input = test_input if test_input else input_for_day(3)
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
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to
use a passphrase instead of simply a password. A passphrase consists of a
series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

  - aa bb cc dd ee is valid.
  - aa bb cc dd aa is not valid - the word aa appears more than once.
  - aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How
many passphrases are valid?

Your puzzle answer was 455.
'''
def day04_1(test_input=None):
    passphrases = test_input if test_input else input_for_day(4)
    return day04_shared(passphrases, 1)

'''
For added security, yet another system policy has been put in place. Now,
a valid passphrase must contain no two words that are anagrams of each
other - that is, a passphrase is invalid if any word's letters can be
rearranged to form any other word in the passphrase.

For example:

  - abcde fghij is a valid passphrase.
  - abcde xyz ecdab is not valid - the letters from the third word can be
    rearranged to form the first word.
  - a ab abc abd abf abj is a valid passphrase, because all letters need
    to be used when forming another word.
  - iiii oiii ooii oooi oooo is valid.
  - oiii ioii iioi iiio is not valid - any of these words can be
    rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

Your puzzle answer was 186.
'''
def day04_2(test_input=None):
    passphrases = test_input if test_input else input_for_day(4)
    return day04_shared(passphrases, 2)

# Day 04 shared code
def day04_shared(passphrases, puzzle):
    valid_passphrases = 0
    for passphrase in passphrases:
        words = passphrase.split(' ')
        if puzzle == 1:
            unique = set(words)
        else:
            unique = set(map(lambda word: ''.join(sorted(list(word))), words))
        if len(unique) == len(words):
            valid_passphrases += 1
    return valid_passphrases

'''
--- Day 5: A Maze of Twisty Trampolines, All Alike ---

An urgent interrupt arrives from the CPU: it's trapped in a maze of jump
instructions, and it would like assistance from any programs with spare
cycles to help find the exit.

The message includes a list of the offsets for each jump. Jumps are
relative: -1 moves to the previous instruction, and 2 skips the next one.
Start at the first instruction in the list. The goal is to follow the
jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump,
the offset of that instruction increases by 1. So, if you come across an
offset of 3, you would move three instructions forward, but change it to
a 4 for the next time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3

Positive jumps ("forward") move downward; negative jumps move upward. For
legibility in this example, these offset values will be written all on
one line, with the current instruction marked in parentheses. The
following steps would be taken before an exit is found:

  - (0) 3  0  1  -3  - before we have taken any steps.
  - (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all).
    Fortunately, the instruction is then incremented to 1.
  -  2 (3) 0  1  -3  - step forward because of the instruction we just
    modified. The first instruction is incremented again, now to 2.
  -  2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
  -  2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
  -  2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

In this example, the exit is reached in 5 steps.

How many steps does it take to reach the exit?

Your puzzle answer was 381680.
'''
def day05_1(test_input=None):
    maze = test_input if test_input else input_for_day(5)
    return day05_shared(maze, 1)

'''
Now, the jumps are even stranger: after each jump, if the offset was
three or more, instead decrease it by 1. Otherwise, increase it by 1 as
before.

Using this rule with the above example, the process now takes 10 steps,
and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

Your puzzle answer was 29717847.
'''
def day05_2(test_input=None):
    maze = test_input if test_input else input_for_day(5)
    return day05_shared(maze, 2)

# Day 05 shared code
def day05_shared(maze, puzzle):
    steps = 0
    position = 0
    while position >= 0 and position < len(maze):
        last_position = position
        position += maze[position]
        increment = 1 if puzzle == 1 or maze[last_position] < 3 else -1
        maze[last_position] += increment
        steps += 1
    return steps

'''
--- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a
memory reallocation routine, but it keeps getting stuck in an infinite
loop.

In this area, there are sixteen memory banks; each memory bank can hold
any number of blocks. The goal of the reallocation routine is to balance
the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the
memory bank with the most blocks (ties won by the lowest-numbered memory
bank) and redistributes those blocks among the banks. To do this, it
removes all of the blocks from the selected bank, then moves to the next
(by index) memory bank and inserts one of the blocks. It continues doing
this until it runs out of blocks; if it reaches the last memory bank, it
wraps around to the first one.

The debugger would like to know how many redistributions can be done
before a blocks-in-banks configuration is produced that has been seen
before.

For example, imagine a scenario with only four memory banks:

  - The banks start with 0, 2, 7, and 0 blocks. The third bank has the
    most blocks, so it is chosen for redistribution.
  - Starting with the next bank (the fourth bank) and then continuing to
    the first bank, the second bank, and so on, the 7 blocks are spread
    out over the memory banks. The fourth, first, and second banks get
    two blocks each, and the third bank gets one back. The final result
    looks like this: 2 4 1 2.
  - Next, the second bank is chosen because it contains the most blocks
    (four). Because there are four memory banks, each gets one block. The
    result is: 3 1 2 3.
  - Now, there is a tie between the first and fourth memory banks, both
    of which have three blocks. The first bank wins the tie, and its
    three blocks are distributed evenly over the other three banks,
    leaving it with none: 0 2 3 4.
  - The fourth bank is chosen, and its four blocks are distributed such
    that each of the four banks receives one: 1 3 4 1.
  - The third bank is chosen, and the same thing happens: 2 4 1 2.

At this point, we've reached a state we've seen before: 2 4 1 2 was
already seen. The infinite loop is detected after the fifth block
redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many
redistribution cycles must be completed before a configuration is
produced that has been seen before?

Your puzzle answer was 12841.
'''
def day06_1(test_input=None):
    banks = test_input if test_input else input_for_day(6)
    return day06_shared(banks, 1)

'''
Out of curiosity, the debugger would also like to know the size of the
loop: starting from a state that has already been seen, how many block
redistribution cycles must be performed before that same state is seen
again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the
answer in that example would be 4.

How many cycles are in the infinite loop that arises from the
configuration in your puzzle input?

Your puzzle answer was 8038.
'''
def day06_2(test_input=None):
    banks = test_input if test_input else input_for_day(6)
    return day06_shared(banks, 2)

# Day 06 shared code
def day06_shared(banks, puzzle):
    num_banks = len(banks)
    visited_states = []
    max_blocks = 0
    max_pos = 0
    cycles = 0
    while banks not in visited_states:
        visited_states.append(banks[:])
        cycles += 1
        for bank in banks:
            if bank > max_blocks:
                max_blocks = bank
                max_pos = banks.index(bank)
        banks[max_pos] = 0
        for offset in range(1, max_blocks + 1):
            banks[(max_pos + offset) % num_banks] += 1
        max_blocks = 0
    if puzzle == 1:
        return cycles
    else:
        return len(visited_states) - visited_states.index(banks)

'''
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a
tower of programs that have gotten themselves into a bit of trouble. A
recursive algorithm has gotten out of hand, and now they're balanced
precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large
disc, and on the disc are balanced several more sub-towers. At the bottom
of these sub-towers, standing on the bottom disc, are other programs,
each holding their own disc, and so on. At the very tops of these sub-
sub-sub-...-towers, many programs stand simply keeping the disc below
them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of
these towers. You ask each program to yell out their name, their weight,
and (if they're holding a disc) the names of the programs immediately
above them balancing on that disc. You write this information down (your
puzzle input). Unfortunately, in their panic, they don't do this in an
orderly fashion; by the time you're done, you're not sure which program
gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

...then you would be able to recreate the structure of the towers that
looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth

In this example, tknk is at the bottom of the tower (the bottom program),
and is holding up ugml, padx, and fwft. Those programs are, in turn,
holding up other programs; in this example, none of those programs are
holding up any other programs, and are all the tops of their own towers.
(The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information
is correct. What is the name of the bottom program?

Your puzzle answer was dtacyn.
'''
def day07_1(test_input=None):
    stacks = test_input if test_input else input_for_day(7)
    callees = set()
    for program in stacks:
        stack = stacks[program]
        for callee in stack['callees']:
            if callee in stacks:
                callees.add(callee)
    return list(set(stacks.keys()).difference(callees))[0]

'''
The programs explain the situation: they can't get down. Rather, they
could get down, if they weren't expending all of their energy trying to
keep the tower balanced. Apparently, one program has the wrong weight,
and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms
a sub-tower. Each of those sub-towers are supposed to be the same weight,
or the disc itself isn't balanced. The weight of a tower is the sum of
the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced,
gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its
disc and all programs above it must each match. This means that the
following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

As you can see, tknk's disc is unbalanced: ugml's stack is heavier than
the other two. Even though the nodes above ugml are balanced, ugml itself
is too heavy: it needs to be 8 units lighter for its stack to weigh 243
and keep the towers balanced. If this change were made, its weight would
be 60.

Given that exactly one program is the wrong weight, what would its weight
need to be to balance the entire tower?

Your puzzle answer was 521.
'''
def day07_2(test_input=None):
    def compute_subtree_weights(node):
        node['subtree_weight'] = node['weight']
        for callee in node['callees']:
            node['subtree_weight'] += compute_subtree_weights(stacks[callee])
        return node['subtree_weight']

    def balance_subtree(node, parent_weight=None):
        subtree = node
        target_weight = 0
        weights = [stacks[callee]['subtree_weight'] for callee in node['callees']]
        if len(weights) > 1:
            target_weight = weights[0 if weights.count(weights[0]) > 1 else 1]
            for callee in node['callees']:
                if stacks[callee]['subtree_weight'] != target_weight:
                    subtree = stacks[callee]
        if subtree != node:
            return balance_subtree(subtree, target_weight)
        else:
            return parent_weight - len(node['callees']) * target_weight

    stacks = test_input if test_input else input_for_day(7)
    root_node = stacks[day07_1()]
    compute_subtree_weights(root_node)
    return balance_subtree(root_node)

'''
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent
assistance with jump instructions, it would like you to compute the
result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify,
whether to increase or decrease that register's value, the amount by
which to increase or decrease it, and a condition. If the condition
fails, skip the instruction without modifying the register. The registers
all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

  - Because a starts at 0, it is not greater than 1, and so b is not
    modified.
  - a is increased by 1 (to 1) because b is less than 5 (it is 0).
  - c is decreased by -10 (to 10) because a is now greater than or equal to
    1 (it is 1).
  - c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth to tell you what all the
registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the
instructions in your puzzle input?

Your puzzle answer was 3089.
'''
def day08_1(test_input=None):
    instructions = test_input if test_input else input_for_day(8)
    return day08_shared(instructions, 1)

'''
To be safe, the CPU also needs to know the highest value held in any
register during this process so that it can decide how much memory to
allocate to these operations. For example, in the above instructions, the
highest value ever held was 10 (in register c after the third instruction
was evaluated).

Your puzzle answer was 5391.
'''
def day08_2(test_input=None):
    instructions = test_input if test_input else input_for_day(8)
    return day08_shared(instructions, 2)

# Day 08 shared code
def day08_shared(instructions, puzzle):
    def eval_cond(c_reg, c_op, c_val):
        if c_op == '==':
            return c_reg_val == c_val
        elif c_op == '!=':
            return c_reg_val != c_val
        elif c_op == '>=':
            return c_reg_val >= c_val
        elif c_op == '>':
            return c_reg_val > c_val
        elif c_op == '<=':
            return c_reg_val <= c_val
        elif c_op == '<':
            return c_reg_val < c_val

    registers = {}
    max_value = 0
    for instruction in instructions:
        (t_reg, t_op, t_val, _, c_reg, c_op, c_val) = instruction.split(' ')
        c_reg_val = int(registers[c_reg]) if c_reg in registers else 0
        t_reg_val = int(registers[t_reg]) if t_reg in registers else 0
        if eval_cond(c_reg, c_op, int(c_val)):
            t_reg_val += int(t_val) if t_op == 'inc' else -int(t_val)
            registers[t_reg] = t_reg_val
            if puzzle == 2 and t_reg_val > max_value:
                max_value = t_reg_val
    return max(registers.values()) if puzzle == 1 else max_value

'''
--- Day 9: Stream Processing ---

A large stream blocks your path. According to the locals, it's not safe
to cross the stream at the moment because it's full of garbage. You look
down at the stream; rather than water, you discover that it's a stream of
characters.

You sit for a while and record part of the stream (your puzzle input).
The characters represent groups - sequences that begin with { and end
with }. Within a group, there are zero or more other things, separated by
commas: either another group or garbage. Since groups can contain other
groups, a } only closes the most-recently-opened unclosed group - that
is, they are nestable. Your puzzle input represents a single, large group
which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. Garbage begins with
< and ends with >. Between those angle brackets, almost any character can
appear, including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, some program has canceled
some of the characters within it using !: inside garbage, any character
that comes after ! should be ignored, including <, >, and even another !.

You don't see any characters that deviate from these rules. Outside
garbage, you only find well-formed groups, and garbage always terminates
according to the rules above.

Here are some self-contained pieces of garbage:

  - <>, empty garbage.
  - <random characters>, garbage containing random characters.
  - <<<<>, because the extra < are ignored.
  - <{!>}>, because the first > is canceled.
  - <!!>, because the second ! is canceled, allowing the > to terminate
    the garbage.
  - <!!!>>, because the second ! and the first > are canceled.
  - <{o"i!a,<{i<a>, which ends at the first >.

Here are some examples of whole streams and the number of groups they
contain:

  - {}, 1 group.
  - {{{}}}, 3 groups.
  - {{},{}}, also 3 groups.
  - {{{},{},{{}}}}, 6 groups.
  - {<{},{},{{}}>}, 1 group (which itself contains garbage).
  - {<a>,<a>,<a>,<a>}, 1 group.
  - {{<a>},{<a>},{<a>},{<a>}}, 5 groups.
  - {{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are
    canceled).

Your goal is to find the total score for all groups in your input. Each
group is assigned a score which is one more than the score of the group
that immediately contains it. (The outermost group gets a score of 1.)

  - {}, score of 1.
  - {{{}}}, score of 1 + 2 + 3 = 6.
  - {{},{}}, score of 1 + 2 + 2 = 5.
  - {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
  - {<a>,<a>,<a>,<a>}, score of 1.
  - {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
  - {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
  - {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.

What is the total score for all groups in your input?

Your puzzle answer was 23588.
'''
def day09_1(test_input=None):
    stream = test_input if test_input else input_for_day(9)
    return day09_shared(stream, 1)

'''
Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters
within the garbage. The leading and trailing < and > don't count, nor do
any canceled characters or the ! doing the canceling.

  - <>, 0 characters.
  - <random characters>, 17 characters.
  - <<<<>, 3 characters.
  - <{!>}>, 2 characters.
  - <!!>, 0 characters.
  - <!!!>>, 0 characters.
  - <{o"i!a,<{i<a>, 10 characters.

How many non-canceled characters are within the garbage in your puzzle
input?

Your puzzle answer was 10045.
'''
def day09_2(test_input=None):
    stream = test_input if test_input else input_for_day(9)
    return day09_shared(stream, 2)

# Day 09 shared code
def day09_shared(stream, puzzle):
    depth = 0
    score = 0
    garbage_count = 0
    cancel_next = False
    in_garbage = False
    for character in stream:
        if cancel_next:
            cancel_next = False
        elif character == '!':
            cancel_next = True
        elif in_garbage:
            if character == '>':
                in_garbage = False
            else:
                garbage_count += 1
        elif character == '{':
            depth += 1
            score += depth
        elif character == '}':
            depth -= 1
        elif character == '<':
            in_garbage = True
    return score if puzzle == 1 else garbage_count

'''
--- Day 10: Knot Hash ---

You come across some programs that are trying to implement a software
emulation of a hash based on knot-tying. The hash these programs are
implementing isn't very strong, but you decide to help them anyway. You
make a mental note to remind the Elves later not to invent their own
cryptographic functions.

This hash function simulates tying a knot in a circle of string with 256
marks on it. Based on the input to be hashed, the function repeatedly
selects a span of string, brings the ends together, and gives the span a
half-twist to reverse the order of the marks within it. After doing this
many times, the order of the marks is used to build the resulting hash.

  4--5   pinch   4  5           4   1
 /    \  5,0,1  / \/ \  twist  / \ / \
3      0  -->  3      0  -->  3   X   0
 \    /         \ /\ /         \ / \ /
  2--1           2  1           2   5

To achieve this, begin with a list of numbers from 0 to 255, a current
position which begins at 0 (the first element in the list), a skip size
(which starts at 0), and a sequence of lengths (your puzzle input). Then,
for each length:

  - Reverse the order of that length of elements in the list, starting
    with the element at the current position.
  - Move the current position forward by that length plus the skip size.
  - Increase the skip size by one.

The list is circular; if the current position and the length try to
reverse elements beyond the end of the list, the operation reverses using
as many extra elements as it needs from the front of the list. If the
current position moves past the end of the list, it wraps around to the
front. Lengths larger than the size of the list are invalid.

Here's an example using a smaller list:

Suppose we instead only had a circular list containing five elements,
0, 1, 2, 3, 4, and were given input lengths of 3, 4, 1, 5.

  - The list begins as [0] 1 2 3 4 (where square brackets indicate the
    current position).
  - The first length, 3, selects ([0] 1 2) 3 4 (where parentheses
    indicate the sublist to be reversed).
  - After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4
    .
  - Then, the current position moves forward by the length, 3, plus the
    skip size, 0: 2 1 0 [3] 4. Finally, the skip size increases to 1.

  - The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
  - The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
  - The current position moves forward by the length plus the skip size,
    a total of 5, causing it not to move because it wraps around:
    4 3 0 [1] 2. The skip size increases to 2.

  - The third length, 1, selects a sublist of a single element, and so
    reversing it has no effect.
  - The current position moves forward by the length (1) plus the skip
    size (2): 4 [3] 0 1 2. The skip size increases to 3.

  - The fourth length, 5, selects every element starting with the second:
    4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4 into 4 2 1 0 3)
    produces: 3) ([4] 2 1 0.
  - Finally, the current position moves forward by 8: 3 4 2 1 [0]. The
    skip size increases to 4.

In this example, the first two numbers in the list end up being 3 and 4;
to check the process, you can multiply them together to produce 12.

However, you should instead use the standard list size of 256 (with
values 0 to 255) and the sequence of lengths in your puzzle input. Once
this process is complete, what is the result of multiplying the first two
numbers in the list?

Your puzzle answer was 11413.
'''
def day10_1(test_input=None):
    lengths = test_input if test_input else input_for_day(10)
    list = [i for i in range(5 if test_input else 256)]
    list = compute_sparse_hash(lengths, 1, list)
    return list[0] * list[1]

'''
The logic you've constructed forms a single round of the Knot Hash
algorithm; running the full thing requires many of these rounds. Some
input and output processing is also required.

First, from now on, your input should be taken not as a list of numbers,
but as a string of bytes instead. Unless otherwise specified, convert
characters to bytes using their ASCII codes. This will allow you to
handle arbitrary ASCII strings, and it also ensures that your input
lengths are never larger than 255. For example, if you are given 1,2,3,
you should convert it to the ASCII codes for each character:
49,44,50,44,51.

Once you have determined the sequence of lengths to use, add the
following lengths to the end of the sequence: 17, 31, 73, 47, 23. For
example, if you are given 1,2,3, your final sequence of lengths should be
49,44,50,44,51,17,31,73,47,23 (the ASCII codes from the input string
combined with the standard length suffix values).

Second, instead of merely running one round like you did above, run a
total of 64 rounds, using the same length sequence in each round. The
current position and skip size should be preserved between rounds. For
example, if the previous example was your first round, you would start
your second round with the same length sequence (
3, 4, 1, 5, 17, 31, 73, 47, 23, now assuming they came from ASCII codes
and include the suffix), but start with the previous round's current
position (4) and skip size (4).

Once the rounds are complete, you will be left with the numbers from 0 to
255 in some order, called the sparse hash. Your next task is to reduce
these to a list of only 16 numbers called the dense hash. To do this, use
numeric bitwise XOR to combine each consecutive block of 16 numbers in
the sparse hash (there are 16 such blocks in a list of 256 numbers). So,
the first element in the dense hash is the first sixteen elements of the
sparse hash XOR'd together, the second element in the dense hash is the
second sixteen elements of the sparse hash XOR'd together, etc.

For example, if the first sixteen elements of your sparse hash are as
shown below, and the XOR operator is ^, you would calculate the first
output number like this:

65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64

Perform this operation on each of the sixteen blocks of sixteen numbers
in your sparse hash to determine the sixteen numbers in your dense hash.

Finally, the standard way to represent a Knot Hash is as a single
hexadecimal string; the final output is the dense hash in hexadecimal
notation. Because each number in your dense hash will be between 0 and
255 (inclusive), always represent each number as two hexadecimal digits
(including a leading zero as necessary). So, if your first three numbers
are 64, 7, 255, they correspond to the hexadecimal numbers 40, 07, ff,
and so the first six characters of the hash would be 4007ff. Because
every Knot Hash is sixteen such numbers, the hexadecimal representation
is always 32 hexadecimal digits (0-f) long.

Here are some example hashes:

  - The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
  - AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
  - 1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
  - 1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.

Treating your puzzle input as a string of ASCII characters, what is the
Knot Hash of your puzzle input? Ignore any leading or trailing
whitespace you might encounter.

Your puzzle answer was 7adfd64c2a03a4968cf708d1b7fd418d.
'''
def day10_2(test_input=None):
    input = test_input if test_input else input_for_day(10, 2)
    lengths = map(lambda character: ord(character), input)
    lengths += [17, 31, 73, 47, 23]
    sparse_hash = compute_sparse_hash(lengths, 64)
    dense_hash = []
    xor_result = 0
    for i in range(256):
        if i > 0 and i % 16 == 0:
            dense_hash.append(xor_result)
            xor_result = 0
        xor_result ^= sparse_hash[i]
    dense_hash.append(xor_result)
    knot_hash = ''
    for hash_element in dense_hash:
        knot_hash += format(hash_element, '02x')
    return knot_hash

# Day 10 shared code
def compute_sparse_hash(lengths, iterations, list=None):
    list = list if list else [i for i in range(256)]
    position = 0
    skip = 0
    for _ in range(iterations):
        for length in lengths:
            if length > 0:
                end = (position + length) % len(list)
                sublist = list[position:end if end > position else len(list)] \
                    + ([] if end > position else list[:end])
                reversed_sublist = sublist[::-1]
                list[position:end if end > position else len(list)] \
                    = reversed_sublist[:length if end > position else length - end]
                if end <= position:
                    list[:end] = reversed_sublist[length - end:]
            position = (position + length + skip) % len(list)
            skip += 1
    return list

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
def day11_1(test_input=None):
    steps = test_input if test_input else input_for_day(11)
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
def day11_2(test_input=None):
    steps = test_input if test_input else input_for_day(11)
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
    return distance

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
def day12_1(test_input=None):
    links = test_input if test_input else input_for_day(12)
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

def day12_1_recursive(test_input=None):
    def linked_to_0(program):
        if program in group_0:
            return True
        else:
            linked = False
            for linked_program in links[program]:
                day12_1_recursive.iterations += 1
                if linked_program not in visiting:
                    visiting.add(linked_program)
                    linked = linked or linked_to_0(linked_program)
                    visiting.remove(linked_program)
            if linked:
                group_0.add(program)
            return linked

    links = test_input if test_input else input_for_day(12)
    group_0 = set('0')
    visiting = set()
    day12_1_recursive.iterations = 0
    for program in links.keys():
        linked_to_0(program)
    print("Iterations: %d" % day12_1_recursive.iterations)
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
def day12_2(test_input=None):
    links = test_input if test_input else input_for_day(12)
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
--- Day 13: Packet Scanners ---

You need to cross a vast firewall. The firewall consists of several
layers, each with a security scanner that moves back and forth across the
layer. To succeed, you must not be detected by a scanner.

By studying the firewall briefly, you are able to record (in your puzzle
input) the depth of each layer and the range of the scanning area for the
scanner within it, written as depth: range. Each layer has a thickness of
exactly 1. A layer at depth 0 begins immediately inside the firewall; a
layer at depth 1 would start immediately after that.

For example, suppose you've recorded the following:

0: 3
1: 2
4: 4
6: 4

This means that there is a layer immediately inside the firewall (with
range 3), a second layer immediately after that (with range 2), a third
layer which begins at depth 4 (with range 4), and a fourth layer which
begins at depth 6 (also with range 4). Visually, it might look like this:

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Within each layer, a security scanner moves back and forth within its
range. Each security scanner starts at the top and moves down until it
reaches the bottom, then moves up until it reaches the top, and repeats.
A security scanner takes one picosecond to move one step. Drawing
scanners as S, the first few picoseconds look like this:

Picosecond 0:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 1:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

Your plan is to hitch a ride on a packet about to move through the
firewall. The packet will travel along the top of each layer, and it
moves at one layer per picosecond. Each picosecond, the packet moves one
layer forward (its first move takes it into layer 0), and then the
scanners move one step. If there is a scanner at the top of the layer as
your packet enters it, you are caught. (If a scanner moves into the top
of its layer while you are there, you are not caught: it doesn't have
time to notice you before you leave.) If you were to do this in the
configuration above, marking your current position with parentheses, your
passage through the firewall would look like this:

Initial state:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 0:
 0   1   2   3   4   5   6
(S) [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
( ) [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 1:
 0   1   2   3   4   5   6
[ ] ( ) ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] (S) ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]


Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] (.) ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] (.) ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]


Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... (.) [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

 0   1   2   3   4   5   6
[S] [S] ... (.) [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]


Picosecond 4:
 0   1   2   3   4   5   6
[S] [S] ... ... ( ) ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... ( ) ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 5:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] (.) [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [S] ... ... [S] (.) [S]
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]


Picosecond 6:
 0   1   2   3   4   5   6
[ ] [S] ... ... [S] ... (S)
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... ( )
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

In this situation, you are caught in layers 0 and 6, because your packet
entered the layer when its scanner was at the top when you entered it.
You are not caught in layer 1, since the scanner moved into the top of
the layer once you were already there.

The severity of getting caught on a layer is equal to its depth
multiplied by its range. (Ignore layers in which you do not get caught.)
The severity of the whole trip is the sum of these values. In the example
above, the trip severity is 0*3 + 6*4 = 24.

Given the details of the firewall you've recorded, if you leave
immediately, what is the severity of your whole trip?

Your puzzle answer was 2384.
'''
def day13_1(test_input=None):
    scan_ranges = test_input if test_input else input_for_day(13)
    penalty = 0
    for depth in scan_ranges.keys():
        scan_range = scan_ranges[depth]
        if depth % (scan_range - 1) == 0 and (depth / (scan_range - 1)) % 2 == 0:
            penalty += depth * scan_range
    return penalty

'''
Now, you need to pass through the firewall without being caught - easier
said than done.

You can't control the speed of the packet, but you can delay it any
number of picoseconds. For each picosecond you delay the packet before
beginning your trip, all security scanners move one step. You're not in
the firewall during this time; you don't enter layer 0 until you stop
delaying the packet.

In the example above, if you delay 10 picoseconds (picoseconds 0 - 9), you won't get caught:

State after delaying:
 0   1   2   3   4   5   6
[ ] [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]


Picosecond 10:
 0   1   2   3   4   5   6
( ) [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
( ) [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 11:
 0   1   2   3   4   5   6
[ ] ( ) ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[S] (S) ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 12:
 0   1   2   3   4   5   6
[S] [S] (.) ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] (.) ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 13:
 0   1   2   3   4   5   6
[ ] [ ] ... (.) [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [S] ... (.) [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]


Picosecond 14:
 0   1   2   3   4   5   6
[ ] [S] ... ... ( ) ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... ( ) ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]


Picosecond 15:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] (.) [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

 0   1   2   3   4   5   6
[S] [S] ... ... [ ] (.) [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]


Picosecond 16:
 0   1   2   3   4   5   6
[S] [S] ... ... [ ] ... ( )
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... ( )
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

Because all smaller delays would get you caught, the fewest number of
picoseconds you would need to delay to get through safely is 10.

What is the fewest number of picoseconds that you need to delay the
packet to pass through the firewall without being caught?

Your puzzle answer was 3921270.
'''
def day13_2(test_input=None):
    scan_ranges = test_input if test_input else input_for_day(13)
    delay = 0
    collisions = 1
    while collisions > 0:
        collisions = 0
        delay += 1
        for depth in scan_ranges.keys():
            scan_range = scan_ranges[depth]
            if (depth + delay) % (scan_range - 1) == 0 and ((depth + delay) / (scan_range - 1)) % 2 == 0:
                collisions += 1
                break
    return delay

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
def day14_1(test_input=None):
    key = test_input if test_input else input_for_day(14)
    used_blocks = 0
    for i in range(0, 128):
        row = day10_2("%s-%d" % (key, i))
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
def day14_2(test_input=None):
    def merge_regions(result_region, redundant_region):
        for (row, column) in regions[redundant_region]:
            regions[result_region].append((row, column))
            region_map[(row, column)] = result_region
        regions.pop(redundant_region)
        return result_region

    key = test_input if test_input else input_for_day(14)
    rows = []
    region_map = {}
    current_region = None
    encountered_regions = 0
    regions = {}
    for i in range(0, 128):
        row = bin(int(day10_2("%s-%d" % (key, i)), 16))[2:]
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
--- Day 15: Dueling Generators ---

Here, you encounter a pair of dueling generators. The generators, called
generator A and generator B, are trying to agree on a sequence of
numbers. However, one of them is malfunctioning, and so the sequences
don't always match.

As they do this, a judge waits for each of them to generate its next
value, compares the lowest 16 bits of both values, and keeps track of the
number of times those parts of the values match.

The generators both work on the same principle. To create its next value,
a generator will take the previous value it produced, multiply it by a
factor (generator A uses 16807; generator B uses 48271), and then keep
the remainder of dividing that resulting product by 2147483647. That
final remainder is the value it produces next.

To calculate each generator's first value, it instead uses a specific
starting value as its "previous value" (as listed in your puzzle input).

For example, suppose that for starting values, generator A uses 65, while
generator B uses 8921. Then, the first five pairs of generated values
are:

--Gen. A--  --Gen. B--
   1092455   430625591
1181022009  1233683848
 245556042  1431495498
1744312007   137874439
1352636452   285222916

In binary, these pairs are (with generator A's value first in each pair):

00000000000100001010101101100111
00011001101010101101001100110111

01000110011001001111011100111001
01001001100010001000010110001000

00001110101000101110001101001010
01010101010100101110001101001010

01100111111110000001011011000111
00001000001101111100110000000111

01010000100111111001100000100100
00010001000000000010100000000100

Here, you can see that the lowest (here, rightmost) 16 bits of the third
value match: 1110001101001010. Because of this one match, after
processing these five pairs, the judge would have added only 1 to its
total.

To get a significant sample, the judge would like to consider 40 million
pairs. (In the example above, the judge would eventually find a total of
588 pairs that match in their lowest 16 bits.)

After 40 million pairs, what is the judge's final count?

Your puzzle answer was 573.
'''
def day15_1(test_input=None, iterations=40000000):
    generator_inputs = test_input if test_input else input_for_day(15)
    factors = {'A': 16807, 'B': 48271}
    divisor = 2147483647
    results = {'A': generator_inputs[0], 'B': generator_inputs[1]}
    binary = {}
    match_count = 0
    for _ in range(0, iterations):
        for generator in ['A', 'B']:
            results[generator] = (results[generator] * factors[generator]) % divisor
            binary[generator] = bin(results[generator])[-16:]
        if binary['A'] == binary['B']:
            match_count += 1
    return match_count

'''
In the interest of trying to align a little better, the generators get
more picky about the numbers they actually give to the judge.

They still generate values in the same way, but now they only hand a
value to the judge when it meets their criteria:

Generator A looks for values that are multiples of 4.
Generator B looks for values that are multiples of 8.

Each generator functions completely independently: they both go through
values entirely on their own, only occasionally handing an acceptable
value to the judge, and otherwise working through the same sequence of
values as before until they find one.

The judge still waits for each generator to provide it with a value
before comparing them (using the same comparison method as before). It
keeps track of the order it receives values; the first values from each
generator are compared, then the second values from each generator, then
the third values, and so on.

Using the example starting values given above, the generators now produce
the following first five values each:

--Gen. A--  --Gen. B--
1352636452  1233683848
1992081072   862516352
 530830436  1159784568
1980017072  1616057672
 740335192   412269392

These values have the following corresponding binary values:

01010000100111111001100000100100
01001001100010001000010110001000

01110110101111001011111010110000
00110011011010001111010010000000

00011111101000111101010001100100
01000101001000001110100001111000

01110110000001001010100110110000
01100000010100110001010101001000

00101100001000001001111001011000
00011000100100101011101101010000

Unfortunately, even though this change makes more bits similar on
average, none of these values' lowest 16 bits match. Now, it's not until
the 1056th pair that the judge finds the first match:

--Gen. A--  --Gen. B--
1023762912   896885216

00111101000001010110000111100000
00110101011101010110000111100000

This change makes the generators much slower, and the judge is getting
impatient; it is now only willing to consider 5 million pairs. (Using the
values from the example above, after five million pairs, the judge would
eventually find a total of 309 pairs that match in their lowest 16 bits.)

After 5 million pairs, but using this new generator logic, what is the
judge's final count?

Your puzzle answer was 294.
'''
def day15_2(test_input=None, max_comparisons=5000000):
    generator_inputs = test_input if test_input else input_for_day(15)
    factors = {'A': 16807, 'B': 48271}
    divisor = 2147483647
    whim_divisors = {'A': 4, 'B': 8}
    values = {'A': generator_inputs[0], 'B': generator_inputs[1]}
    results = {'A': [], 'B': []}
    offset = 0
    comparisons = 0
    match_count = 0
    while comparisons < max_comparisons:
        for generator in ['A', 'B']:
            values[generator] = (values[generator] * factors[generator]) % divisor
            if values[generator] % whim_divisors[generator] == 0:
                results[generator].append(bin(values[generator])[-16:])
        if min(len(results['A']), len(results['B'])) > offset:
            comparisons += 1
            if results['A'][offset] == results['B'][offset]:
                match_count += 1
            offset += 1
    return match_count

'''
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be
dancing.

There are sixteen programs in total, named a through p. They start by
standing in a line: a stands in position 0, b stands in position 1, and
so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

  - Spin, written sX, makes X programs move from the end to the front,
    but maintain their order otherwise. (For example, s3 on abcde
    produces cdeab).
  - Exchange, written xA/B, makes the programs at positions A and B swap
    places.
  - Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they
could do the following dance:

  - s1, a spin of size 1: eabcd.
  - x3/4, swapping the last two programs: eabdc.
  - pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle
input). In what order are the programs standing after their dance?

Your puzzle answer was kbednhopmfcjilag.
'''
def day16_1(test_input=None, start_state=None):
    moves = test_input if test_input else input_for_day(16)
    programs = list(start_state) if start_state else list('abcdefghijklmnop')
    for move in moves:
        move_type = move[0]
        instruction = move[1:]
        if move_type == 's':
            tail = programs[-int(instruction):]
            head = programs[:16 - int(instruction)]
            programs = tail + head
        elif move_type == 'x':
            (a, b) = instruction.split('/')
            program_a = programs[int(a)]
            program_b = programs[int(b)]
            programs[int(a)] = program_b
            programs[int(b)] = program_a
        else:
            (program_a, program_b) = instruction.split('/')
            index_a = programs.index(program_a)
            index_b = programs.index(program_b)
            programs[index_a] = program_b
            programs[index_b] = program_a
    return ''.join(programs)

'''
Now that you're starting to get a feel for the dance moves, you turn your
attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the
programs perform it again and again: including the first dance, a total
of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc
, and use the same dance moves:

  - s1, a spin of size 1: cbaed.
  - x3/4, swapping the last two programs: cbade.
  - pe/b, swapping programs e and b: ceadb.

In what order are the programs standing after their billion dances?

Your puzzle answer was fbmcgdnjakpioelh.
'''
def day16_2():
    start_state = 'abcdefghijklmnop'
    states = [start_state]
    found_period = False
    period = 0
    while not found_period:
        period += 1
        states.append(day16_1(None, states[period - 1]))
        found_period = states[-1] == start_state
    remainder = 1000000000 % period
    return states[remainder]

'''
--- Day 17: Spinlock ---

Suddenly, whirling in the distance, you notice what looks like a massive,
pixelated hurricane: a deadly spinlock. This spinlock isn't just consuming
computing power, but memory, too; vast, digital mountains are being ripped
from the ground and consumed by the vortex.

If you don't move quickly, fixing that printer will be the least of your
problems.

This spinlock's algorithm is simple but efficient, quickly consuming
everything in its path. It starts with a circular buffer containing only
the value 0, which it marks as the current position. It then steps forward
through the circular buffer some number of steps (your puzzle input)
before inserting the first new value, 1, after the value it stopped on.
The inserted value becomes the current position. Then, it steps forward
from there the same number of steps, and wherever it stops, inserts after
it the second new value, 2, and uses that as the new current position
again.

It repeats this process of stepping forward, inserting a new value, and
using the location of the inserted value as the new current position a
total of 2017 times, inserting 2017 as its final operation, and ending
with a total of 2018 values (including 0) in the circular buffer.

For example, if the spinlock were to step 3 times per insert, the circular
buffer would begin to evolve like this (using parentheses to mark the
current position after each iteration of the algorithm):

  - (0), the initial state before any insertions.
  - 0 (1): the spinlock steps forward three times (0, 0, 0), and then
    inserts the first value, 1, after it. 1 becomes the current position.
  - 0 (2) 1: the spinlock steps forward three times (0, 1, 0), and then
    inserts the second value, 2, after it. 2 becomes the current position.
  - 0  2 (3) 1: the spinlock steps forward three times (1, 0, 2), and then
    inserts the third value, 3, after it. 3 becomes the current position.

And so on:

  - 0  2 (4) 3  1
  - 0 (5) 2  4  3  1
  - 0  5  2  4  3 (6) 1
  - 0  5 (7) 2  4  3  6  1
  - 0  5  7  2  4  3 (8) 6  1
  - 0 (9) 5  7  2  4  3  8  6  1

Eventually, after 2017 insertions, the section of the circular buffer near
the last insertion looks like this:

1512  1134  151 (2017) 638  1513  851

Perhaps, if you can identify the value that will ultimately be after the
last value written (2017), you can short-circuit the spinlock. In this
example, that would be 638.

What is the value after 2017 in your completed circular buffer?

Your puzzle answer was 1642.
'''
def day17_1(test_input=None):
    steps = test_input if test_input else input_for_day(17)
    position = 0
    spinlock = [position]
    value = 1
    while value < 2018:
        position = (position + (steps % value)) % value
        spinlock.insert(position + 1, value)
        position += 1
        value += 1
    return spinlock[position + 1]

'''
The spinlock does not short-circuit. Instead, it gets more angry. At
least, you assume that's what happened; it's spinning significantly faster
than it was a moment ago.

You have good news and bad news.

The good news is that you have improved calculations for how to stop the
spinlock. They indicate that you actually need to identify the value after
0 in the current state of the circular buffer.

The bad news is that while you were determining this, the spinlock has
just finished inserting its fifty millionth value (50000000).

What is the value after 0 the moment 50000000 is inserted?

Your puzzle answer was 33601318.
'''
def day17_2(test_input=None):
    steps = test_input if test_input else input_for_day(17)
    position = 0
    value = 1
    value_at_1 = 0
    while value < 50000000:
        position = (position + (steps % value)) % value
        if position == 0:
            value_at_1 = value
        position += 1
        value += 1
    return value_at_1

#
# ADDITIONAL FUNCTIONS
#

'''
--- Day 18: Duet ---

You discover a tablet containing some strange assembly code labeled simply
"Duet". Rather than bother the sound card with it, you decide to run the
code yourself. Unfortunately, you don't see any documentation, so you're
left to figure out what the instructions mean on your own.

It seems like the assembly is meant to operate on a set of registers that
are each named with a single letter and that can each hold a single
integer. You suppose each register should start with a value of 0.

There aren't that many instructions, so it shouldn't be hard to figure out
what they do. Here's what you determine:

  - snd X plays a sound with a frequency equal to the value of X.
  - set X Y sets register X to the value of Y.
  - add X Y increases register X by the value of Y.
  - mul X Y sets register X to the result of multiplying the value
    contained in register X by the value of Y.
  - mod X Y sets register X to the remainder of dividing the value
    contained in register X by the value of Y (that is, it sets X to the
    result of X modulo Y).
  - rcv X recovers the frequency of the last sound played, but only when
    the value of X is not zero. (If it is zero, the command does nothing.)
  - jgz X Y jumps with an offset of the value of Y, but only if the value
    of X is greater than zero. (An offset of 2 skips the next instruction,
    an offset of -1 jumps to the previous instruction, and so on.)

Many of the instructions can take either a register (a single letter) or a
number. The value of a register is the integer it contains; the value of a
number is that number.

After each jump instruction, the program continues with the instruction to
which the jump jumped. After any other instruction, the program continues
with the next instruction. Continuing (or jumping) off either end of the
program terminates it.

For example:

set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2

  - The first four instructions set a to 1, add 2 to it, square it, and
    then set it to itself modulo 5, resulting in a value of 4.
  - Then, a sound with frequency 4 (the value of a) is played.
  - After that, a is set to 0, causing the subsequent rcv and jgz
    instructions to both be skipped (rcv because a is 0, and jgz because a
    is not greater than 0).
  - Finally, a is set to 1, causing the next jgz instruction to activate,
    jumping back two instructions to another jump, which jumps again to
    the rcv, which ultimately triggers the recover operation.

At the time the recover operation is executed, the frequency of the last
sound played is 4.

What is the value of the recovered frequency (the value of the most
recently played sound) the first time a rcv instruction is executed with a
non-zero value?

Your puzzle answer was 9423.
'''
def day18_1(test_input=None):
    def int_or_register(value):
        try:
            return int(value)
        except ValueError:
            return registers[value]

    instructions = test_input if test_input else input_for_day(18)
    registers = {}
    last_sound_played = None
    step = 0
    while step in range(0, len(instructions)):
        instruction = instructions[step]
        elements = instruction.split(' ')
        operator = elements[0]
        register = elements[1]
        if register not in registers:
            registers[register] = 0
        value = int_or_register(elements[2]) if len(elements) > 2 else None
        did_jump = False
        if operator == 'snd':
            last_sound_played = registers[register]
        elif operator == 'set':
            registers[register] = value
        elif operator == 'add':
            registers[register] += value
        elif operator == 'mul':
            registers[register] *= value
        elif operator == 'mod':
            registers[register] %= value
        elif operator == 'rcv':
            if registers[register] > 0:
                return last_sound_played
        elif operator == 'jgz':
            if registers[register] > 0:
                step += value
                did_jump = True
        print("%s %s" % (instruction, registers))
        if not did_jump:
            step += 1

'''
As you congratulate yourself for a job well done, you notice that the
documentation has been on the back of the tablet this entire time. While
you actually got most of the instructions correct, there are a few key
differences. This assembly code isn't about sound at all - it's meant to
be run twice at the same time.

Each running copy of the program has its own set of registers and follows
the code independently - in fact, the programs don't even necessarily run
at the same speed. To coordinate, they use the send (snd) and receive (rcv
) instructions:

  - snd X sends the value of X to the other program. These values wait in
    a queue until that program is ready to receive them. Each program has
    its own message queue, so a program can never receive a message it
    sent.
  - rcv X receives the next value and stores it in register X. If no
    values are in the queue, the program waits for a value to be sent to
    it. Programs do not continue to the next instruction until they have
    received a value. Values are received in the order they are sent.

Each program also has its own program ID (one 0 and the other 1); the
register p should begin with this value.

For example:

snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d

Both programs begin by sending three values to the other. Program 0 sends
1, 2, 0; program 1 sends 1, 2, 1. Then, each program receives a value
(both 1) and stores it in a, receives another value (both 2) and stores it
in b, and then each receives the program ID of the other program (program
0 receives 1; program 1 receives 0) and stores it in c. Each program now
sees a different value in its own copy of register c.

Finally, both programs try to rcv a fourth time, but no data is waiting
for either of them, and they reach a deadlock. When this happens, both
programs terminate.

It should be noted that it would be equally valid for the programs to run
at different speeds; for example, program 0 might have sent all three
values and then stopped at the first rcv before program 1 executed even
its first instruction.

Once both of your programs have terminated (regardless of what caused them
to do so), how many times did program 1 send a value?

Your puzzle answer was 7620.
'''
def day18_2(test_input=None):
    def int_or_register(value):
        try:
            return int(value)
        except ValueError:
            return registers[program][value]

    instructions = test_input if test_input else input_for_day(18)
    registers = {0: {'p': 0}, 1: {'p': 1}}
    queue = [[], []]
    state = [1, 1]  # 1: running; 0: waiting; -1: terminated
    step = [0, 0]
    program = 0
    snd_count = [0, 0]
    while True:
        instruction = instructions[step[program]]
        elements = instruction.split(' ')
        operator = elements[0]
        register = elements[1]
        if register not in registers[program]:
            registers[program][register] = 0
        value = int_or_register(elements[2]) if len(elements) > 2 else None
        did_jump = False
        did_swap = False
        if operator == 'snd':
            queue[1 - program].append(registers[program][register])
            snd_count[program] += 1
        elif operator == 'set':
            registers[program][register] = value
        elif operator == 'add':
            registers[program][register] += value
        elif operator == 'mul':
            registers[program][register] *= value
        elif operator == 'mod':
            registers[program][register] %= value
        elif operator == 'rcv':
            if len(queue[program]) > 0:
                registers[program][register] = queue[program].pop(0)
                state[program] = 1
            else:
                if state[1 - program] == -1:
                    break
                if state[1 - program] == 0 and len(queue[1 - program]) == 0:
                    break
                state[program] = 0
                program = 1 - program
                did_swap = True
        elif operator == 'jgz':
            if int_or_register(register) > 0:
                step[program] += value
                did_jump = True
        if not did_jump and not did_swap:
            step[program] += 1
        if step[program] not in range(0, len(instructions)):
            if state[1 - program] == -1:
                break
            state[program] = -1
            program = 1 - program
    return snd_count[1]

'''
--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to
follow a routing diagram (your puzzle input), but it's confused about
where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |
, -, and +) show the path it needs to take, starting by going down onto
the only line connected to the top of the diagram. It needs to follow this
path until it reaches the end (located somewhere within the diagram) and
stop there.

Sometimes, the lines cross over each other; in these cases, it needs to
continue going the same direction, and only turn left or right when
there's no other option. In addition, someone has left letters on the
line; these also don't change its direction, but it can use them to keep
track of where it's been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

  - Starting at the only line touching the top of the diagram, it must go
    down, pass through A, and continue onward to the first +.
  - Travel right, up, and right, passing through B in the process.
  - Continue down (collecting C), right, and up (collecting D).
  - Finally, go all the way left through E and stopping at F.

Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way.
What letters will it see (in the order it would see them) if it follows
the path? (The routing diagram is very wide; make sure you view it without
line wrapping.)

Your puzzle answer was EOCZQMURF.
'''
def day19_1(test_input=None):
    diagram = test_input if test_input else input_for_day(19)
    return day19_shared(diagram, 1)

'''
The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|--|-E---+
     |  |  |  D
     +B-+  +--+

...the packet would go:

  - 6 steps down (including the first line at the top of the diagram).
  - 3 steps right.
  - 4 steps up.
  - 3 steps right.
  - 4 steps down.
  - 3 steps right.
  - 2 steps up.
  - 13 steps left (including the F it stops on).

This would result in a total of 38 steps.

How many steps does the packet need to go?

Your puzzle answer was 16312.
'''
def day19_2(test_input=None):
    diagram = test_input if test_input else input_for_day(19)
    return day19_shared(diagram, 2)

# Day 19 shared code
def day19_shared(diagram, puzzle):
    (y, x) = (0, 0)
    while diagram[y][x] != '|':
        x += 1
    delta_y = 1
    delta_x = 0
    letters = ''
    steps = 1
    while x in range(len(diagram[y])) and y in range(len(diagram)):
        if diagram[y][x] == '+':
            if delta_y != 0:
                delta_y = 0
                delta_x = 1 if diagram[y][x + 1] != ' ' else -1
            else:
                delta_y = 1 if diagram[y + 1][x] != ' ' else -1
                delta_x = 0
        elif diagram[y][x] == ' ':
            break
        elif diagram[y][x] in 'ABCDEFGHIjKlMNOPQRSTUVWXYZ':
            letters = letters + diagram[y][x]
        y += delta_y
        x += delta_x
        steps += 1
    return letters if puzzle == 1 else steps - 1

'''
--- Day 20: Particle Swarm ---

Suddenly, the GPU contacts you, asking for help. Someone has asked it to
simulate too many particles, and it won't be able to finish them all in
time to render the next frame at this rate.

It transmits to you a buffer (your puzzle input) listing each particle in
order (starting with particle 0, then particle 1, particle 2, and so on).
For each particle, it provides the X, Y, and Z coordinates for the
particle's position (p), velocity (v), and acceleration (a), each in the
format <X,Y,Z>.

Each tick, all particles are updated simultaneously. A particle's
properties are updated in the following order:

  - Increase the X velocity by the X acceleration.
  - Increase the Y velocity by the Y acceleration.
  - Increase the Z velocity by the Z acceleration.
  - Increase the X position by the X velocity.
  - Increase the Y position by the Y velocity.
  - Increase the Z position by the Z velocity.

Because of seemingly tenuous rationale involving z-buffering, the GPU
would like to know which particle will stay closest to position <0,0,0> in
the long term. Measure this using the Manhattan distance, which in this
situation is simply the sum of the absolute values of a particle's X, Y,
and Z position.

For example, suppose you are only given two particles, both of which stay
entirely on the X-axis (for simplicity). Drawing the current states of
particles 0 and 1 (in that order) with an adjacent a number line and
diagram of current X positions (marked in parenthesis), the following
would take place:

p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)

p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)

p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)

p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)

At this point, particle 1 will never be closer to <0,0,0> than particle 0,
and so, in the long run, particle 0 will stay closest.

Which particle will stay closest to position <0,0,0> in the long term?

Your puzzle answer was 258.
'''
def day20_1(test_input=None):
    states = test_input if test_input else input_for_day(20)
    min_a = 100000000
    min_p = 0
    for p in range(len(states)):
        a = abs(states[p][2][0]) + abs(states[p][2][1]) + abs(states[p][2][2])
        if a < min_a:
            min_a = a
            min_p = p
    return min_p

'''
To simplify the problem further, the GPU would like to remove any
particles that collide. Particles collide if their positions ever exactly
match. Because particles are updated simultaneously, more than two
particles can collide at the same time and place. Once particles collide,
they are removed and cannot collide with anything else after that tick.

For example:

p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)
p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)
p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>

------destroyed by collision------
------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
------destroyed by collision------                      (3)
p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>

In this example, particles 0, 1, and 2 are simultaneously destroyed at the
time and place marked X. On the next tick, particle 3 passes through
unharmed.

How many particles are left after all collisions are resolved?

Your puzzle answer was 707.
'''
def day20_2(test_input=None):
    states = test_input if test_input else input_for_day(20)
    annihilated_particles = []
    remaining_count = 0
    flatline_count = 0
    while True:
        occupied_positions = {}
        for p in range(len(states)):
            if p not in annihilated_particles:
                pos = states[p][0]
                v = states[p][1]
                a = states[p][2]
                v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
                pos = (pos[0] + v[0], pos[1] + v[1], pos[2] + v[2])
                if pos in occupied_positions:
                    occupied_positions[pos].append(p)
                else:
                    occupied_positions[pos] = [p]
                    states[p][0] = pos
                    states[p][1] = v
        for position in occupied_positions:
            if len(occupied_positions[position]) > 1:
                for p in occupied_positions[position]:
                    annihilated_particles.append(p)
        last_remaining_count = remaining_count
        remaining_count = (len(states) - len(annihilated_particles))
        if remaining_count == last_remaining_count:
            flatline_count += 1
            if flatline_count > 100:
                break
    return remaining_count

'''
Load input for given day from file and prepare for processing
'''
def input_for_day(day, puzzle=1):
    input = open('input2017/day%02d.txt' % day, 'r').read()
    if day == 1:
        return input
    elif day == 2:
        rows = input.split('\n')
        prepared_input = []
        for row in rows:
            prepared_input.append(map(lambda cell: int(cell), row.split('\t')))
        return prepared_input
    elif day == 3:
        return int(input)
    elif day == 4:
        return input.split('\n')
    elif day == 5:
        return map(lambda i: int(i), input.split('\n'))
    elif day == 6:
        return map(lambda i: int(i), input.split('\t'))
    elif day == 7:
        lines = input.split('\n')
        stacks = {}
        for line in lines:
            parts = line.split(') ->')
            (name, weight) = parts[0].split(' (')
            stacks[name] = {
                'weight': int(weight),
                'callees': parts[1][1:].split(', ')
            } if len(parts) > 1 else {
                'weight': int(weight[:-1]),
                'callees': []
            }
        return stacks
    elif day == 8:
        return input.split('\n')
    elif day == 9:
        return input
    elif day == 10:
        if puzzle == 1:
            return map(lambda length: int(length), input.split(','))
        else:
            return input
    elif day == 11:
        return input.split(',')
    elif day == 12:
        links = {}
        links_s = input.split('\n')
        for link_s in links_s:
            (program, linked_programs) = link_s.split(' <-> ')
            links[program] = linked_programs.split(', ')
        return links
    elif day == 13:
        layer_depths = {}
        for layer_depth in input.split('\n'):
            (layer, depth) = layer_depth.split(': ')
            layer_depths[int(layer)] = int(depth)
        return layer_depths
    elif day == 14:
        return input
    elif day == 15:
        generator_input_strings = input.split('\n')
        generator_inputs = []
        for generator_input_string in generator_input_strings:
            generator_inputs.append(int(generator_input_string.split(' ')[-1]))
        return generator_inputs
    elif day == 16:
        return input.split(',')
    elif day == 17:
        return int(input)
    elif day == 18:
        return input.split('\n')
    elif day == 19:
        return [list(row) for row in input.split('\n')]
    elif day == 20:
        state_strings = input.split('\n')
        states = []
        for state_string in state_strings:
            vector_strings = state_string.split(', ')
            vectors = []
            for vector_string in vector_strings:
                vector_coords = vector_string.split('<')[1].split('>')[0]
                vectors.append(tuple([int(n) for n in vector_coords.split(',')]))
            states.append(vectors)
        return states

'''
Print out results for:

  - an individual puzzle: day > 0; puzzle > 0
  - an indivitual day: day > 0
  - all puzzles so far: no parameters
'''
def aoc(day=None, puzzle=None):
    funcs = {
        1: {1: day01_1, 2: day01_2},
        2: {1: day02_1, 2: day02_2},
        3: {1: day03_1, 2: day03_2},
        4: {1: day04_1, 2: day04_2},
        5: {1: day05_1, 2: day05_2},
        6: {1: day06_1, 2: day06_2},
        7: {1: day07_1, 2: day07_2},
        8: {1: day08_1, 2: day08_2},
        9: {1: day09_1, 2: day09_2},
        10: {1: day10_1, 2: day10_2},
        11: {1: day11_1, 2: day11_2},
        12: {1: day12_1, 2: day12_2},
        13: {1: day13_1, 2: day13_2},
        14: {1: day14_1, 2: day14_2},
        15: {1: day15_1, 2: day15_2},
        16: {1: day16_1, 2: day16_2},
        17: {1: day17_1, 2: day17_2},
        18: {1: day18_1, 2: day18_2},
        19: {1: day19_1, 2: day19_2},
        20: {1: day20_1, 2: day20_2},
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
