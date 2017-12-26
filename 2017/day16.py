import aocinput

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
def puzzle_1(test_input=None, start_state=None):
    moves = test_input if test_input else aocinput.input_for_day(16)
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
def puzzle_2():
    start_state = 'abcdefghijklmnop'
    states = [start_state]
    found_period = False
    period = 0
    while not found_period:
        period += 1
        states.append(puzzle_1(None, states[period - 1]))
        found_period = states[-1] == start_state
    remainder = 1000000000 % period
    return states[remainder]

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
