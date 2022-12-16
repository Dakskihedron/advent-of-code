with open('inputs/day-6.txt', 'r') as file:
    data = file.read().strip()


# Part one
def calculate_char(data, packet_length):
    chars = packet_length
    for n in range(0, len(data)):
        packet = data[n:n+packet_length]
        if len(set(packet)) == len(packet):
            return chars
        chars += 1
        
print('Part 1:', calculate_char(data, 4))


# Part two
print('Part 2:', calculate_char(data, 14))