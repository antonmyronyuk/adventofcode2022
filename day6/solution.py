with open('input.txt') as input_file:
    signal = input_file.read().strip()


def get_packet_start(signal, size):
    return next(
        i + size
        for i in range(len(signal) - size)
        if len(set(signal[i:i + size])) == size
    )


print(get_packet_start(signal, 4))  # part 1
print(get_packet_start(signal, 14))  # part 2
