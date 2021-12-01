

with open('data.txt', 'r') as fh:
    # Part 1
    data = [int(line.strip()) for line in fh.readlines()]

    pivot = data[0]
    depth_increases = 0

    for idx in range(1, len(data)):
        if data[idx] > data[idx-1]:
            depth_increases += 1

    print(f'{depth_increases=}')

    # Part 2
    fn_depth_increases = 0
    for idx in range(3, len(data)):
        window_a = sum(data[idx-3:idx])
        window_b = sum(data[idx-2:idx+1])

        if window_b > window_a:
            fn_depth_increases += 1

    print(f'{fn_depth_increases=}')
