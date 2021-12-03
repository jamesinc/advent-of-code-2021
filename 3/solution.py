def most_common_bit(bits):
    avg = sum(bits) / len(bits)

    return round(avg)
def least_common_bit(bits):
    avg = sum(bits) / len(bits)

    return 0 if round(avg) else 1

with open('data.txt', 'r') as fh:
    # Part 1
    data = [line.strip() for line in fh.readlines()]
    bits = [[int(bit) for bit in col] for col in zip(*data)]

    most_common_bits = [str(most_common_bit(col)) for col in bits]
    least_common_bits = [str(least_common_bit(col)) for col in bits]
    print(f'0b{"".join(most_common_bits)}')
    print(f'0b{"".join(least_common_bits)}')
    gamma_rate = int(f'0b{"".join(most_common_bits)}', 2)
    epsilon_rate = int(f'0b{"".join(least_common_bits)}', 2)
    print(gamma_rate)
    print(epsilon_rate)
    print(gamma_rate *  epsilon_rate)
