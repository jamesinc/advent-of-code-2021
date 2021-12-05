
def load_data(filename):

    with open(filename, 'r') as fh:
        return [line.strip() for line in fh.readlines()]

def bin_to_int(bin_str):

    return int(f'0b{bin_str}', 2)

def most_common_bit(data, col=None, p2=False):
    bits = [int(x[col]) for x in data] if col is not None else [int(x) for x in data]
    avg = sum(bits) / len(bits)

    return str(1 if avg == 0.5 and p2 else round(avg))

def least_common_bit(data, col=None, p2=False):
    bits = [int(x[col]) for x in data] if col is not None else [int(x) for x in data]
    avg = sum(bits) / len(bits)

    return str(0 if avg == 0.5 and p2 else [1, 0][round(avg)])

def part_one_rates(data):
    data = [] + data
    bits_by_column = [col for col in zip(*data)]
    most_common_bits = [most_common_bit(col) for col in bits_by_column]
    least_common_bits = [least_common_bit(col) for col in bits_by_column]
    gamma_rate = bin_to_int("".join(most_common_bits))
    epsilon_rate = bin_to_int("".join(least_common_bits))

    return gamma_rate, epsilon_rate

def part_two_rates(data):
    o2_data = [] + data
    co2_data = [] + data
    o2_bits_by_column = [[int(bit) for bit in col] for col in zip(*o2_data)]
    co2_bits_by_column = [[int(bit) for bit in col] for col in zip(*co2_data)]

    # O2 rating
    for c_idx in range(len(o2_bits_by_column)):
        pass_bit = most_common_bit(o2_data, c_idx, p2=True)

        for o2_idx in reversed(range(len(o2_data))):
            if len(o2_data) == 1:
                break

            if o2_data[o2_idx][c_idx] != pass_bit:
                o2_data.pop(o2_idx)

    # CO2 scrubber rating
    for c_idx in range(len(co2_bits_by_column)):
        pass_bit = least_common_bit(co2_data, c_idx, p2=True)

        for co2_idx in reversed(range(len(co2_data))):
            if len(co2_data) == 1:
                break

            if co2_data[co2_idx][c_idx] != pass_bit:
                co2_data.pop(co2_idx)

    return bin_to_int(o2_data[0]), bin_to_int(co2_data[0])

# Part 1
sample_data = load_data('sample.txt')
sample_gamma, sample_epsilon = part_one_rates(sample_data)
assert sample_gamma == 22, f'Gamma rate incorrect, expected 22 got {sample_gamma}'
assert sample_epsilon == 9, f'Epsilon rate incorrect, expected 9 got {sample_epsilon}'

data = load_data('data.txt')
gamma_rate, epsilon_rate = part_one_rates(data)

print(f'Part 1 solution: {gamma_rate * epsilon_rate}')

# Part 2
sample_o2_rating, sample_co2_rating = part_two_rates(sample_data)

assert sample_o2_rating == 23, f'O2 rating incorrect, expected 23 got {sample_o2_rating}'
assert sample_co2_rating == 10, f'CO2 rating incorrect, expected 10 got {sample_co2_rating}'

o2_rating, co2_rating = part_two_rates(data)

print(f'Part 2 solution: {o2_rating * co2_rating}')