
with open('data.txt', 'r') as fh:
    # Part 1
    data = [int(line.strip()) for line in fh.readlines()]

    depth_increases = 0

    for idx in range(1, len(data)):
        depth_increases += data[idx] > data[idx-1]

    print(f'{depth_increases=}')

    # Part 2
    fn_depth_increases = 0

    for idx in range(3, len(data)):
        fn_depth_increases += sum(data[idx-2:idx+1]) > sum(data[idx-3:idx])

    print(f'{fn_depth_increases=}')
