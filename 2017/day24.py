import aocinput

'''
--- Day 24: Electromagnetic Moat ---

The CPU itself is a large, black building surrounded by a bottomless pit.
Enormous metal tubes extend outward from the side of the building at
regular intervals and descend down into the void. There's no way to cross,
but you need to get inside.

No way, of course, other than building a bridge out of the magnetic
components strewn about nearby.

Each component has two ports, one on each end. The ports come in all
different types, and only matching types can be connected. You take an
inventory of the components by their port types (your puzzle input). Each
port is identified by the number of pins it uses; more pins mean a
stronger connection for your bridge. A 3/7 component, for example, has a
type-3 port on one side, and a type-7 port on the other.

Your side of the pit is metallic; a perfect surface to connect a magnetic,
zero-pin port. Because of this, the first port you use must be of type 0.
It doesn't matter what type of port you end with; your goal is just to
make the bridge as strong as possible.

The strength of a bridge is the sum of the port types in each component.
For example, if your bridge is made of components 0/3, 3/7, and 7/4, your
bridge has a strength of 0+3 + 3+7 + 7+4 = 24.

For example, suppose you had the following components:

0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10

With them, you could make the following valid bridges:

  - 0/1
  - 0/1--10/1
  - 0/1--10/1--9/10
  - 0/2
  - 0/2--2/3
  - 0/2--2/3--3/4
  - 0/2--2/3--3/5
  - 0/2--2/2
  - 0/2--2/2--2/3
  - 0/2--2/2--2/3--3/4
  - 0/2--2/2--2/3--3/5

(Note how, as shown by 10/1, order of ports within a component doesn't
matter. However, you may only use each port on a component once.)

Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength
of 0+1 + 1+10 + 10+9 = 31.

What is the strength of the strongest bridge you can make with the
components you have available?

Your puzzle answer was 1940.
'''
def puzzle_1(test_input=None):
    def bridge_strength(bridge):
        strength = 0
        for component in bridge:
            strength += component[0] + component[1]
        return strength

    def continue_bridge(bridge, required_pin):
        sub_bridges = []
        for component in components:
            if component not in bridge and required_pin in component:
                next_pin = component[1 if component[0] == required_pin else 0]
                sub_bridges.append(continue_bridge(bridge + [component], next_pin))
        if len(sub_bridges) == 0:
            return bridge
        max_strength = 0
        strongest_bridge = []
        for sub_bridge in sub_bridges:
            strength = bridge_strength(sub_bridge)
            if strength > max_strength:
                max_strength = strength
                strongest_bridge = sub_bridge
        return strongest_bridge

    components = test_input if test_input else aocinput.input_for_day(24)
    return bridge_strength(continue_bridge([], 0))

'''
The bridge you've built isn't long enough; you can't jump the rest of the
way.

In the example above, there are two longest bridges:

  - 0/2--2/2--2/3--3/4
  - 0/2--2/2--2/3--3/5

Of them, the one which uses the 3/5 component is stronger; its strength is
0+2 + 2+2 + 2+3 + 3+5 = 19.

What is the strength of the longest bridge you can make? If you can make
multiple bridges of the longest length, pick the strongest one.

Your puzzle answer was 1928.
'''
def puzzle_2(test_input=None):
    def bridge_strength(bridge):
        strength = 0
        for component in bridge:
            strength += component[0] + component[1]
        return strength

    def continue_bridge(bridge, required_pin):
        sub_bridges = []
        for component in components:
            if component not in bridge and required_pin in component:
                next_pin = component[1 if component[0] == required_pin else 0]
                sub_bridges.append(continue_bridge(bridge + [component], next_pin))
        if len(sub_bridges) == 0:
            return bridge
        max_length = 0
        max_strength = 0
        longest_bridge = []
        for sub_bridge in sub_bridges:
            length = len(sub_bridge)
            if length > max_length:
                max_length = length
                longest_bridge = sub_bridge
            elif length == max_length:
                strength = bridge_strength(sub_bridge)
                if strength > max_strength:
                    max_strength = strength
                    longest_bridge = sub_bridge
        return longest_bridge

    components = test_input if test_input else aocinput.input_for_day(24)
    return bridge_strength(continue_bridge([], 0))

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())
