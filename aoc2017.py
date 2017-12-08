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

def day03_1(test_input = 0):
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
'''
def day03_2(test_input = 0):
    input = test_input if test_input else input_for_day(3)
    mem = { (0, 0): 1 }
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
'''
def day04_1(test_input = 0):
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
'''
def day04_2(test_input = 0):
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
'''
def day05_1(test_input = 0):
    maze = test_input if test_input else input_for_day(5)
    return day05_shared(maze, 1)

'''
Now, the jumps are even stranger: after each jump, if the offset was
three or more, instead decrease it by 1. Otherwise, increase it by 1 as
before.

Using this rule with the above example, the process now takes 10 steps,
and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
'''
def day05_2(test_input = 0):
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
'''
def day06_1(test_input = 0):
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
'''
def day06_2(test_input = 0):
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
'''
def day07_1(test_input = 0):
    stacks = test_input if test_input else input_for_day(7)
    callees = set()
    for program in stacks:
        stack = stacks[program]
        if 'callees' in stack:
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


'''
def day07_2(test_input = 0):
    def compute_subtree_weights(node):
        node['subtree_weight'] = node['weight']
        for callee in node['callees']:
            node['subtree_weight'] += compute_subtree_weights(stacks[callee])
        return node['subtree_weight']
            
    def balance_subtree(node, parent_weight = None):
        subtree = node
        target_weight = 0
        weights = []
        for callee in node['callees']:
            weights.append(stacks[callee]['subtree_weight'])
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
'''
def day08_1(test_input = 0):
    instructions = test_input if test_input else input_for_day(8)
    return day08_shared(instructions, 1)

'''
To be safe, the CPU also needs to know the highest value held in any
register during this process so that it can decide how much memory to
allocate to these operations. For example, in the above instructions, the
highest value ever held was 10 (in register c after the third instruction
was evaluated).
'''
def day08_2(test_input = 0):
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
        
#
# HELPER FUNCTIONS
#

'''
Print out results for:

  - an individual puzzle: day > 0; puzzle > 0
  - an indivitual day: day > 0
  - all puzzles so far: no parameters
'''
def aoc(day = 0, puzzle = 0):
    funcs = {
         1: {1: day01_1, 2: day01_2},
         2: {1: day02_1, 2: day02_2},
         3: {1: day03_1, 2: day03_2},
         4: {1: day04_1, 2: day04_2},
         5: {1: day05_1, 2: day05_2},
         6: {1: day06_1, 2: day06_2},
         7: {1: day07_1, 2: day07_2},
         8: {1: day08_1, 2: day08_2},
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
Load input for given day from file and prepare for processing
'''
def input_for_day(day):
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
        
        