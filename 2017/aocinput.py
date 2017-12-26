'''
Load input for given day from file and prepare for processing
'''
def input_for_day(day, puzzle=1):
    input = open('input/day%02d.txt' % day, 'r').read()
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
    elif day == 21:
        rules = {}
        for rule_string in input.split('\n'):
            (match_pattern, result_pattern) = rule_string.split(' => ')
            rules[tuple(match_pattern.split('/'))] = result_pattern.split('/')
        return rules
    elif day == 22:
        rows = input.split('\n')
        extent = len(rows) / 2
        memory_map = {}
        for row in range(-extent, extent + 1):
            row_map = {}
            for col in range(-extent, extent + 1):
                row_map[col] = rows[row + extent][col + extent]
            memory_map[-row] = row_map
        return memory_map
    elif day == 23:
        return input.split('\n')
    elif day == 24:
        components = []
        for component in input.split('\n'):
            components.append([int(pins) for pins in component.split('/')])
        return components
