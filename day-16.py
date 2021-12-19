import numpy as np

with open('inputs/day-16.txt') as file:
    data = file.read()

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}


# Part one
packet = ''.join([hex_to_bin[x] for x in data])
version_sum = 0

def parse_packet(packet):
    global version_sum
    version, typeid, packet = int(packet[:3], 2), int(packet[3:6], 2), packet[6:]
    version_sum += version
    count = 6
    if typeid == 4:
        while True:
            if packet[0] == '0':
                packet = packet[5:]
                count += 5
                break
            packet = packet[5:]
            count += 5
    else:
        len_id, packet = packet[0], packet[1:]
        count += 1
        if len_id == '0':
            len_bits, packet = int(packet[:15], 2), packet[15:]
            len_count = 0
            count += 15
            while len_count < len_bits:
                packet, count  = parse_packet(packet)
                if len(packet) < 6:
                    break
                len_count += count
        else:
            len_bits, packet = int(packet[:11], 2), packet[11:]
            len_bits = (len(packet) // len_bits * len_bits)
            count += 11
            len_count = 0
            while len_count < len_bits:
                packet, count  = parse_packet(packet)
                if len(packet) < 6:
                    break
                len_count += count
    return packet, count

parse_packet(packet)
print(version_sum)


# Part two (and technically part one improved)
packet = ''.join([hex_to_bin[x] for x in data])
version_sum = 0

def parse_literal(packet):
    literal = ''
    while packet[0] != '0':
        literal += packet[1:5]
        packet = packet[5:]
    literal += packet[1:5]
    packet = packet[5:]
    return int(literal, 2), packet 

def parse_operator(typeid, values):
    match typeid:
        case 0:
            return sum(values)
        case 1:
            return np.prod(np.array(values))
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            return int(values[0] > values[1])
        case 6:
            return int(values[0] < values[1])
        case 7:
            return int(values[0] == values[1])

def parse_packet(packet):
    global version_sum
    version, typeid, packet = int(packet[:3], 2), int(packet[3:6], 2), packet[6:]
    version_sum += version
    if typeid == 4:
        literal, packet = parse_literal(packet)
    else:
        len_id, packet = packet[0], packet[1:]
        if len_id == '0':
            packet_len, packet = int(packet[:15], 2), packet[15:]
            values, final_len = [], len(packet) - packet_len
            while len(packet) > final_len:
                value, packet = parse_packet(packet)
                values.append(value)
        else:
            packet_count, packet = int(packet[:11], 2), packet[11:]
            values, curr_count = [], 0
            while curr_count != packet_count:
                value, packet = parse_packet(packet)
                values.append(value)
                curr_count += 1
        literal = parse_operator(typeid, values)
    return literal, packet

value, packet = parse_packet(packet)
print(version_sum)
print(value)