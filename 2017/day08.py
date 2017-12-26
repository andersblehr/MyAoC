import aocinput

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
def puzzle_1(test_input=None):
    instructions = test_input if test_input else aocinput.input_for_day(8)
    return day08_shared(instructions, 1)

'''
To be safe, the CPU also needs to know the highest value held in any
register during this process so that it can decide how much memory to
allocate to these operations. For example, in the above instructions, the
highest value ever held was 10 (in register c after the third instruction
was evaluated).

Your puzzle answer was 5391.
'''
def puzzle_2(test_input=None):
    instructions = test_input if test_input else aocinput.input_for_day(8)
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
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
