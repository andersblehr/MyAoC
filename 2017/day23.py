#!/usr/bin/env python

import aocinput

'''
--- Day 23: Coprocessor Conflagration ---

You decide to head directly to the CPU and fix the printer from there. As
you get close, you find an experimental coprocessor doing so much work
that the local programs are afraid it will halt and catch fire. This would
cause serious issues for the rest of the computer, so you head in and see
what you can do.

The code it's running seems to be a variant of the kind you saw recently
on that tablet. The general functionality seems very similar, but some of
the instructions are different:

  - set X Y sets register X to the value of Y.
  - sub X Y decreases register X by the value of Y.
  - mul X Y sets register X to the result of multiplying the value
    contained in register X by the value of Y.
  - jnz X Y jumps with an offset of the value of Y, but only if the value
    of X is not zero. (An offset of 2 skips the next instruction, an
    offset of -1 jumps to the previous instruction, and so on.)

Only the instructions listed above are used. The eight registers here,
named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows
for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul
instruction invoked?

Your puzzle answer was 3025.
'''
def puzzle_1(test_input=None):
    def int_or_register(value):
        try:
            return int(value)
        except ValueError:
            return registers[value]

    instructions = test_input if test_input else aocinput.input_for_day(23)
    registers = {}
    step = 0
    mul_count = 0
    while True:
        instruction = instructions[step]
        elements = instruction.split(' ')
        operator = elements[0]
        register = elements[1]
        if register not in registers:
            registers[register] = 0
        value = int_or_register(elements[2]) if len(elements) > 2 else None
        did_jump = False
        if operator == 'set':
            registers[register] = value
        elif operator == 'sub':
            registers[register] -= value
        elif operator == 'mul':
            registers[register] *= value
            mul_count += 1
        elif operator == 'mod':
            registers[register] %= value
        elif operator == 'jnz':
            if int_or_register(register) != 0:
                step += value
                did_jump = True
        if not did_jump:
            step += 1
        if step not in range(0, len(instructions)):
            break
    return mul_count

'''
Now, it's time to fix the problem.

The debug mode switch is wired directly to register a. You flip the
switch, which makes register a now start at 1 when the program is
executed.

Immediately, the coprocessor begins to overheat. Whoever wrote this
program obviously didn't choose a very efficient implementation. You'll
need to optimize the program if it has any hope of completing before Santa
needs that printer working.

The coprocessor's ultimate goal is to determine the final value left in
register h once the program completes. Technically, if it had that... it
wouldn't even need to run the program.

After setting register a to 1, if the program were to run to completion,
what value would be left in register h?

Your puzzle answer was 915.
'''

# SOLUTION NOTES - LOOP IDENTIFICATION
#
#   set b 57
#   set c b
# j jnz a 2       *
# j jnz 1 5       | *
#   mul b 100  <--+ |
#   sub b -100000   |
#   set c b         |
#   sub c -17000    |
#   set f 1    <----+<--+
#   set d 2             |
#   set e 2    <------+ |
#   set g d    <----+ | |
#   mul g e         | | |
#   sub g b         | | |
# j jnz g 2       * | | |
#   set f 0       | | | |
#   sub e -1   <--+ | | |
#   set g e         | | |
#   sub g b         | | |
# j jnz g -8        * | |
#   sub d -1          | |
#   set g d           | |
#   sub g b           | |
# j jnz g -13         * |
# j jnz f 2       *     |
#   sub h -1      |     |
#   set g b    <--+     |
#   sub g c             |
# j jnz g 2       *     |
# j jnz 1 3       | *   |
#   sub b -17  <--+ |   |
# j jnz 1 -23       |   *
#                   x

def puzzle_2_dissassembly():
    (b, c, h) = (105700, 122700, 0)  # steps 1-8
    (d, e, f, g) = (0, 0, 0, 0)
    while True:
        f = 1                        # set f 1
        d = 2                        # set d 2
        while g <= 0:
            e = 2                    # set e 2
            while g <= 0:
                g = d * e - b        # set g d; mul g e; sub g b
                if g == 0:           # jnz g 2
                    f = 0            # set f 0
                e += 1               # sub e -1
                g = e - b            # set g e; sub g b
            d += 1                   # sub d -1
            g = d - b                # seg g d; sub g b
        if f == 0:                   # jnz f 2
            h += 1                   # sub h -1
        g = b - c                    # set g b; sub g c
        if g == 0:                   # jnz g 2
            break                    # jnz 1 3
        b += 17                      # sub b -17
    return h

def puzzle_2_dissassembly_optimized():
    (b, c, h) = (105700, 122700, 0)
    for n in range(b, c + 1, 17):
        f = 1
        for i in range(2, b + 1):
            for j in range(2, b + 1):
                if i * j == n:
                    f = 0
        if f == 0:
            h += 1
    return h

def puzzle_2():
    (b, c, h) = (105700, 122700, 0)
    for n in range(b, c + 1, 17):
        for f in range(2, n / 2):
            if n % f == 0:
                h += 1
                break
    return h

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
