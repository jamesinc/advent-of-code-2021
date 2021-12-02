
def coords(coords_string):
    dir, amt = coords_string.split()
    if dir == 'forward':
        return [int(amt), 0]
    else:
        return [0, int(amt) * (1 if dir =='up' else -1)]

with open('data.txt', 'r') as fh:
    # Part 1
    data = [coords(line.strip()) for line in fh.readlines()]

    totals = [sum(x) for x in zip(*data)]

    print(totals[0] * abs(totals[1]))

    # Part 2
    position = [0, 0]
    aim = 0

    for datum in data:
        # Do aim calc first
        aim += datum[1]
        # Add to horizontal position
        position[0] += datum[0]
        # Calculate new depth based on 
        position[1] += datum[0] * aim

    print(position[0] * abs(position[1]))