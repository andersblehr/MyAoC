import aocinput

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
def puzzle_1(test_input=None):
    states = test_input if test_input else aocinput.input_for_day(20)
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
def puzzle_2(test_input=None):
    states = test_input if test_input else aocinput.input_for_day(20)
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
        if len(states) - len(annihilated_particles) == remaining_count:
            flatline_count += 1
            if flatline_count > 100:
                break
        else:
            remaining_count = len(states) - len(annihilated_particles)
    return remaining_count

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
